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
simDuration = 2000

# Initialize an array to store sensor values over time:
backLegSensorValues = np.zeros(simDuration)
frontLegSensorValues = np.zeros(simDuration)

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

# Step the world:
for t in range(simDuration):
    # print(f"t={t}")
    p.stepSimulation()
    backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/240)
    
p.disconnect()

## POST SIMULATION ##

# Save the sensor data:
np.save("data/results/backLegSensorValues.npy",backLegSensorValues)
np.save("data/results/frontLegSensorValues.npy",frontLegSensorValues)