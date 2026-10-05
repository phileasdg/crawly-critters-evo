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
            print(t)
            # # print(f"t={t}")
            p.stepSimulation()
            # backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            
            # # Front leg
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotID,
            #     jointName=b"Torso_FrontLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=frontLegTargetAngles[t],
            #     maxForce=50)

            # # Back leg
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotID,
            #     jointName=b"Torso_BackLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=backLegTargetAngles[t],
            #     maxForce=50)
            
            time.sleep(c.frameDuration)
            
            # p.disconnect()