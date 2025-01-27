### we need to import some python modules from the $SUMO_HOME/tools directory
import os
import sys
import optparse

# %% Set properly your working directory, the path to collect the outputs (Stats) and the XML demand file
WorkingDirectory = "/Users/pa.laharotte/LICIT_LAB Dropbox/PA LAHAROTTE/LICIT_202004_/_COURS/ITS/_TP_Environment/24-25-test-practical-exercises/Project07-GLOSA-test/simulation_sumo/"
os.chdir(WorkingDirectory)
print(os.getcwd())

outputFolder = './outputs/'
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

demandXMLFile = "traffic_light_rou_glosa.rou.xml"
# Please note that you have to change manually the demand values
MPR = 100
glosa_range = 1000

# %% Set the path to your SUMO_HOME
os.environ['SUMO_HOME'] = "/usr/local/opt/sumo/share/sumo" # 'Users\eleonore\sumo' # /path/to/your/SUMO_HOME # on Mac, the usual path is: '/usr/local/opt/sumo/share/sumo'

####################################################################

# %% DO NOT TOUCH IT! Automatic process to adapt the configuration file of SUMO: 
# change the configuration file of SUMO to include the specified folder dedicated to output collection
import xml.etree.ElementTree as ET
# https://docs.python.org/3/library/xml.etree.elementtree.html

cfgFileName = "traffic_light_sim.sumocfg"

xmlTree = ET.parse(cfgFileName)
rootElement = xmlTree.getroot()
# rootElement.tag

# Identify the tags to update
dictOutputFileByTag = {
    "input": {"route-files": demandXMLFile},
    "output": {"tripinfo-output": "trip_info_test_mpr"+str(MPR)+"range"+str(glosa_range)+".xml",
               "summary-output":  "summary_mpr"+str(MPR)+"range"+str(glosa_range)+".xml",
               "queue-output": "queue_mpr"+str(MPR)+"range"+str(glosa_range)+".xml",
               "fcd-output":  "FCD_test_mpr"+str(MPR)+"range"+str(glosa_range)+".xml",
               "emission-output":  "emission_test_mpr"+str(MPR)+"range"+str(glosa_range)+".xml"
               }
    }

#Iterate Through All Tags
for tag in dictOutputFileByTag.keys(): # ["tripinfo-output", "emission-output", "summary-output", "amitran-output", "fcd-output"]:
    for element in rootElement.findall(tag):
        #NoNeeds : # Check if title contains the word Python
        #NoNeeds:  if 'Python' in element.find('title').text :
        #Change xml attribute value
        if tag=="input":
            subtag = list(dictOutputFileByTag[tag])[0]
            for subelement in element.findall(subtag):
                subelement.set('value', dictOutputFileByTag[tag][subtag])
        elif tag=="output":
            for subtag in list(dictOutputFileByTag[tag]):
                for subelement in element.findall(subtag):
                    subelement.set('value', outputFolder+dictOutputFileByTag[tag][subtag])

#Write the modified file.        
xmlTree.write(cfgFileName,encoding='UTF-8',xml_declaration=True) 



# %%
import os

change_directory = "cd '" + WorkingDirectory + "'"
execute_scenario = "sumo -c traffic_light_sim.sumocfg --device.glosa.range "+str(glosa_range)

os.system(change_directory)
os.system(execute_scenario)

# Convert to csv files
for subtag in list(dictOutputFileByTag["output"]):
    os.system("python ./xml/xml2csv.py " + outputFolder + dictOutputFileByTag["output"][subtag])
    print("converted to csv - file " + dictOutputFileByTag["output"][subtag])

