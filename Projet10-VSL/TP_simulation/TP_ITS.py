### we need to import some python modules from the $SUMO_HOME/tools directory
import os
import sys
import optparse

# %% Set properly your working directory, the path to collect the outputs (Stats) and the XML demand file
WorkingDirectory = "C:/Users/eleon/OneDrive - entpe.fr/Documents/these/ITS/Projet09-VSL/TP_simulation"
os.chdir(WorkingDirectory)
print(os.getcwd())

outputFolder = './stats_bas/'
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

demandXMLFile = "demand.rou.xml" 

# %% Set the path to your SUMO_HOME
os.environ['SUMO_HOME'] = 'Users\eleonore\sumo' # /path/to/your/SUMO_HOME # on Mac, the usual path is: '/usr/local/opt/sumo/share/sumo'

####################################################################

# %% DO NOT TOUCH IT! Automatic process to adapt the configuration file of SUMO: 
# change the configuration file of SUMO to include the specified folder dedicated to output collection
import xml.etree.ElementTree as ET

cfgFileName = "simulation_vsl.sumocfg"

xmlTree = ET.parse(cfgFileName)
rootElement = xmlTree.getroot()

# Identify the tags to update
dictOutputFileByTag = {"route-files": demandXMLFile,
    "tripinfo-output": "tripinfo.xml", 
    "emission-output": "emissionStats.xml",
    "summary-output": "summaryStats.xml",
    "amitran-output": "trajectoriesStats.xml", 
    "fcd-output": "fcdStats.xml"}

#Iterate Through All Tags
for tag in dictOutputFileByTag.keys(): # ["tripinfo-output", "emission-output", "summary-output", "amitran-output", "fcd-output"]:
    for element in rootElement.findall(tag):
        #NoNeeds : # Check if title contains the word Python
        #NoNeeds:  if 'Python' in element.find('title').text :
        #Change xml attribute value
        if tag=="route-files":
            element.set('value', dictOutputFileByTag[tag])
        else:
            element.set('value', outputFolder+dictOutputFileByTag[tag])

#Write the modified file.        
xmlTree.write(cfgFileName,encoding='UTF-8',xml_declaration=True) 



# %% DO NOT TOUCH! Some codes to import libraries and check your SUMO_HOME's content
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true", default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


####################################################################




# %% SOME USEFUL FUNCTIONS
## VSL system function 
def activate_VSL_system(position1, position2, time1, time2, limitated_veh_list, speed_limit, step):
    """activate the speed limit to all connected vehicle between position1 and position2 between time1 and time2"""
    
    if len(limitated_veh_list)>0:
        for veh in limitated_veh_list: # remove vehicles out of the range with speed restrictions
            if traci.vehicle.getPosition(veh)[0] > position2:
                traci.vehicle.setMaxSpeed(veh, 33.11)
                limitated_veh_list.remove(veh)

        if step>=time2:
            for veh in limitated_veh_list: # remove the speed restriction when the time is elapsed
                traci.vehicle.setMaxSpeed(veh, 33.11)
                limitated_veh_list.remove(veh)
                
    if time2 > step >= time1: # between 5 and 10 min

        running_veh = traci.vehicle.getIDList()  # get the list of vehicles currently driving on the network at this time-step
            
        for veh in running_veh : # loop on vehicles currently driving on the network
            if traci.vehicle.getTypeID(veh) == 'CV': # check if the vehicle is a connected vehicle
                if not veh in limitated_veh_list: # check if the vehicle is in the exclusion list, composed of vehicles already applying a speed restriction
                    if position1 <= traci.vehicle.getPosition(veh)[0] <= position2: # check that the vehicle is in the activation area
                           traci.vehicle.setMaxSpeed(veh, speed_limit) # change the speed limit of the vehicle
                           limitated_veh_list += [veh]
            
        
    
    return limitated_veh_list

        
        
## def lane change system
def activate_lane_changing(position1, position2, time1, time2, limitated_veh_list, step):
    """activate lane changing to all connected vehicle between position1 and position2 between time1 and time2"""
    if time2 > step >= time1: # between 5 and 10 min

        running_veh = traci.vehicle.getIDList()
            
        for veh in running_veh : 
            if traci.vehicle.getTypeID(veh) == 'CV':
                if not veh in limitated_veh_list:
                    if position1 <= traci.vehicle.getPosition(veh)[0] <= position2:
                            if traci.vehicle.getLaneIndex(veh) == 0:
                                traci.vehicle.changeLane(veh, 1, time2-time1)
                                limitated_veh_list += [veh]
            
    return limitated_veh_list

### Simulation 

def run():
    """execute the TraCI control loop"""

    #Constants
    SPEED_LIMIT = 80/3.6 #speed limit is 80 kph = 80/3.6 m/s

    #Inititalisation
    limitated_veh_list = []
    veh_lane0 = []
    veh_lane1 = []
    
    step = 0

    #Run
    while traci.simulation.getMinExpectedNumber() >0:
        traci.simulationStep()

        ### Uncomment this part in question 1.1.2
        ### VSL system to limitate speed of all Connected Vehicles between 2000 and 5000m between 5 and 10 min
        ##limitated_veh_list = activate_VSL_system(2000, 5000, 600, 1200, limitated_veh_list, SPEED_LIMIT, step)
        ##print('number of limitated vehicles', len(limitated_veh_list))
        

        ### Uncomment this part in question 2.2
        ### System to activate lane changing to all Connected Vehicles between 2000 and 5000m between 5 and 10min 
        ##lane_changing_veh_list = activate_lane_changing(2000, 5000, 600, 1200, limitated_veh_list, step)
        ##print(len(lane_changing_veh_list))

        step += 1
        print(step)


    traci.close()
    sys.stdout.flush()


# %%  This is the main entry point of this script: 
# it is what is automatically launched/executed, when this python file is called from the prompt terminal (ie execute `python TP_ITS.py` in the terminal).
# In such case, the python script get the tag "__main__"  in the prompt terminal and the following codes are executed.
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo 
    #as a server, then connect and run

    if options.nogui: # if option --nogui is activate, when executing teh pyhton file in the prompt 
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    
    #traci.start([sumoBinary, "-c", "simulation_name.sumocfg", "--seed", seed_number])
    traci.start([sumoBinary, "-c", "simulation_vsl.sumocfg", "--seed", str(30)])
    run()
