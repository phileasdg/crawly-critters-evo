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
    # Tell pyrosim where to save the geometry:
    pyrosim.Start_URDF("body.urdf")
    # Root link: Torso
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5],size=[1,1,1])
    # BackLeg
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1.0,0,1.0])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5],size=[1,1,1])
    # FrontLeg
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2.0,0,1.0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5],size=[1,1,1])

    pyrosim.End()

# Create the world
Create_World()

# Create the robot
Create_Robot()