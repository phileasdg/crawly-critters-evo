import pyrosim.pyrosim as pyrosim
import pybullet as p

class ROBOT:
    def __init__(self):
        self.sensors={}
        self.motors={}
        # (the robot geometry)
        self.robotID=p.loadURDF("data/robots/body.urdf")

        # Prepare to simulate the robots 
        # This command is required whenever you use sensors or motors.
        pyrosim.Prepare_To_Simulate(self.robotID)