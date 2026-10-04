## DEPENDENCIES ##

# Ludobots requirements:
import pyrosim.pyrosim as pyrosim

# My own imports:
from coming_from_wl import *
import os
import numpy as np

## FILE SETUP ##

# Set the save path to be the folder containing this file:
os.chdir(os.path.dirname(__file__))

## WORLD AND ROBOT GENERATION ##

# Define a function to generate the world geometry:
def Create_World():
    # Tell pyrosim where to save the geometry:
    pyrosim.Start_SDF("world.sdf")

    # Send a cube to the world:
    pyrosim.Send_Cube(
        name="Box",
        pos=[-2,2,.5], 
        size=[1,1,1])

    # Close the SDF file and write it to disk:
    pyrosim.End()
        

# Define a function to generate the a virtual robot to put in the world:
def Create_Robot(position=[0.5,0,0.5],n_links=3):
    # Compute the complete list of required absolute and relative link and joint positions:
    root_link=np.array(position)
    links=[root_link]
    joints=[]
    for i in range(n_links-1):
        joints.append(np.array([1, 0, 1] if i == 0 else [1, 0, 0]))
        links.append(np.array([0.5, 0, 0.5 if i % 2 == 0 else -0.5]))

    # Tell pyrosim where to save the geometry:
    pyrosim.Start_URDF("body.urdf")
    
    # Define the robot body:
    for i, pos in enumerate(links):
        pyrosim.Send_Cube(name=f"Link{i}", pos=pos, size=[1, 1, 1])
    for i, pos in enumerate(joints):
        pyrosim.Send_Joint(name=f"Link{i}_Link{i+1}", parent=f"Link{i}", child=f"Link{i+1}", type="revolute", position=pos)

    pyrosim.End()

# Create the world
Create_World()

# Create the robot
Create_Robot()