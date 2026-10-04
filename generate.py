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
def Create_Robot():
    # Absolute positions: [link, joint, link, ...]:
    chain=[[0, 0, 0.5], [0, 0, 1], [0, 0, 1.5], [0, 0, 2], [0, 0, 2.5], [0, 0.5, 2.5], [0, 1, 2.5], [0, 1.5, 2.5], [0, 2, 2.5], [0, 2, 2], [0, 2, 1.5], [0, 2, 1], [0, 2, 0.5]]
    # Unzip the chain into the lists for links and joints:
    absolute_links = np.array(chain[::2])
    absolute_joints = np.array(chain[1::2])
    
    # Compute the relative positions for all links and joints that are downstream from 
    # the root link and root joint, relative to each element's upstream joint:
    rel_links=absolute_links[1:]-absolute_joints # This works because every link is directly preceded by a joint.
    rel_joints=np.diff(absolute_joints,axis=0) # Differences between consecutive joints.

    # Tell pyrosim where to save the geometry:
    pyrosim.Start_URDF("body.urdf")
    
    # Define the robot body:
    pyrosim.Send_Cube(name="Link0",pos=absolute_links[0],size=[1,1,1]) # Root link    
    pyrosim.Send_Joint(name="Link0_Link1",parent="Link0",child="Link1",type="revolute",position=absolute_joints[0]) # Root joint
    for i, pos in enumerate(rel_joints,start=1):
        pyrosim.Send_Joint(name=f"Link{i}_Link{i+1}",parent=f"Link{i}",child=f"Link{i+1}",type="revolute",position=pos)
    for i, pos in enumerate(rel_links,start=1):
        pyrosim.Send_Cube(name=f"Link{i}",pos=pos,size=[1,1,1]) 
        
    pyrosim.End()

# Create the world
Create_World()

# Create the robot
Create_Robot()