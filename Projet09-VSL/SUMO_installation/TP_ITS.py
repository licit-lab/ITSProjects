### we need to import some python modules from the $SUMO_HOME/tools directory
import os
import sys
import optparse

# %% Set properly your working directory and the path to your SUMO_HOME
WorkingDirectory = "path/to/your/working/directory/"
os.chdir(WorkingDirectory)
print(os.getcwd())

os.environ['SUMO_HOME'] = 'Users\eleonore\sumo' # /path/to/your/SUMO_HOME # on Mac, the usual path is: '/usr/local/opt/sumo/share/sumo'

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
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options



# %% ## Function to run the Simulation 

def run():
    """execute the TraCI control loop"""

    step = 0
    while traci.simulation.getMinExpectedNumber() >0:
        traci.simulationStep()
        
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

    if options.nogui: # if option --nogui is added, when executing the code
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    
    #traci.start([sumoBinary, "-c", "simulation_name.sumocfg", "--seed", seed_number])
    traci.start([sumoBinary, "-c", "init_simulation.sumocfg", "--seed", str(30)])
    run()
