import posix
from coming_from_wl import echo
import os
import pyrosim.pyrosim as pyrosim
from coming_from_wl import *

# Set the save path to be the folder containing this file:
os.chdir(os.path.dirname(__file__))

# Define a function to generate the world geometry:
def Create_World():
    # Tell pyrosim where to save the geometry:
    pyrosim.Start_SDF("world.sdf")

    # Send a cube to the world
    pyrosim.Send_Cube(
        name="Box",
        pos=[-2,2,.5], 
        size=[1,1,1])

    # Close the SDF file and write it to disk:
    pyrosim.End()

# Define a function to generate the a virtual robot to put in the world:
def Create_Robot():
    # Tell pyrosim where to save the geometry:
    pyrosim.Start_URDF("body.urdf")
    # Define the robot body:
    pyrosim.Send_Cube(name="Torso",pos=[0,0,0.5],size=[1,1,1]) # Link
    pyrosim.Send_Joint(name="Torso_Leg",parent="Torso",child="Leg",type="revolute",position=[0,0,1.0]) # Joint
    pyrosim.Send_Cube(name="Leg",pos=[0,0,0.5],size=[1,1,1]) # Link
    pyrosim.End()

# Create the world
Create_World()

# Create the robot
Create_Robot()