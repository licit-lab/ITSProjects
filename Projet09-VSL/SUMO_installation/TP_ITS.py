### we need to import some python modules from the $SUMO_HOME/tools directory
import os
import sys
import optparse

os.environ['SUMO_HOME'] = 'Users\eleonore\sumo'

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



### Simulation 

def run():
    """execute the TraCI control loop"""

    step = 0
    while traci.simulation.getMinExpectedNumber() >0:
        traci.simulationStep()
        
        step += 1
        print(step)


    traci.close()
    sys.stdout.flush()


# This is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo 
    #as a server, then connect and run

    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    
    #traci.start([sumoBinary, "-c", "simulation_name.sumocfg", "--seed", seed_number])
    traci.start([sumoBinary, "-c", "simulation.sumocfg", "--seed", str(30)])
    run()