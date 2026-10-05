## DEPENDENCIES ##

# Ludobots requirements:
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np

# My own imports:
import os

## FILE SETUP ##

os.chdir(os.path.dirname(__file__))

## SIMULATION SETUP ##

# 1. Simulation Parameters: #

# Simulation duration (ticks):
simDuration = 10000
# Frame duration (in seconds):
frameDuration = 1/2000#1/240

# Sensor arrays (to store sensor values over time):
backLegSensorValues = np.zeros(simDuration)
frontLegSensorValues = np.zeros(simDuration)

# Target motor angles:
frontLegAmplitude=np.pi/4
frontLegFrequency=50
frontLegPhaseOffset=0
backLegAmplitude=np.pi/4
backLegFrequency=50
backLegPhaseOffset=np.pi/2
frontLegTargetAngles = np.interp(frontLegAmplitude*np.sin(frontLegFrequency*np.linspace(0,2*np.pi,simDuration)),[-1,1],[-np.pi/4,np.pi/4])
backLegTargetAngles = np.interp(backLegAmplitude*np.sin(backLegFrequency*np.linspace(0,2*np.pi,simDuration)+backLegPhaseOffset),[-1,1],[-np.pi/4,np.pi/4])
np.save("data/results/frontLegTargetAngles.npy",frontLegTargetAngles)
np.save("data/results/backLegTargetAngles.npy",backLegTargetAngles)

# 2. Simulation Environment Setup #

# Connect to the physics sim GUI:
physicsClient = p.connect(p.GUI)

# Tell PyBullet where to look for files:
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Optional: disable the GUI sidebars
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

## WORLD SETUP ##

# Set gravity:
p.setGravity(0,0,-9.8)
# p.setGravity(0,0,-9.8,physicsClient) # (Just in case we need to specify the client explicitly)

# Import geometry 
# (a floor)
planeId = p.loadURDF("plane.urdf")
# (the world geometry)
p.loadSDF("data/worlds/world.sdf")
# (the robot geometry)
robotID=p.loadURDF("data/robots/body.urdf")

# Prepare to simulate the robots 
# This command is required whenever you use sensors or motors.
pyrosim.Prepare_To_Simulate(robotID)

## SIMULATION LOOP ##
# Headstart (to give me time to start recording my video)
p.stepSimulation()
time.sleep(3)
# Step the world:
for t in range(simDuration):
    # print(f"t={t}")
    p.stepSimulation()
    backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    # Front leg
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName=b"Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegTargetAngles[t],
        maxForce=50)

    # Back leg
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName=b"Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegTargetAngles[t],
        maxForce=50)
    
    time.sleep(frameDuration)
    
p.disconnect()

## POST SIMULATION ##

# Save the sensor data:
np.save("data/results/backLegSensorValues.npy",backLegSensorValues)
np.save("data/results/frontLegSensorValues.npy",frontLegSensorValues)