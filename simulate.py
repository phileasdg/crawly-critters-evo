## DEPENDENCIES ##

# Ludobots requirements:
import pybullet as p
import pybullet_data
import time

# My own imports:
import os

## FILE SETUP ##

os.chdir(os.path.dirname(__file__))

## SIMULATION SETUP ##

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
p.loadSDF("world.sdf")
# (the robot geometry)
p.loadURDF("body.urdf")

## SIMULATION LOOP ##

# Step the world:
for t in range(5000):
    print(f"t={t}")
    p.stepSimulation()
    time.sleep(1/240)
    
p.disconnect()