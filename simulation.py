from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time

class SIMULATION:
    def __init__(self):
        # Simulation Environment Setup

        # Connect to the physics sim GUI:
        self.physicsClient = p.connect(p.GUI)

        # Tell PyBullet where to look for files:
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Optional: disable the GUI sidebars
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        ## WORLD SETUP ##
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.simDuration):
            # print(f"t={t}")
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            time.sleep(c.frameDuration)
            
    def __del__(self):
        p.disconnect()