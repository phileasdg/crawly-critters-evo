from pyrosim import pyrosim
import pybullet as p
import numpy as np
import constants as c

class MOTOR:
    def __init__(self,jointName):
        self.jointName=jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude=c.amplitude
        self.frequency=c.frequency
        self.offset=c.phaseOffset
        self.motorValues=self.amplitude*np.sin(self.frequency*np.linspace(0,2*np.pi,c.simDuration)+self.offset)

    def Set_Value(self,robot,t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=50)
            