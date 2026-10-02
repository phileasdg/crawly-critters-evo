import posix
from coming_from_wl import echo
import os
import pyrosim.pyrosim as pyrosim
from coming_from_wl import *

# Set the save path to be the folder containing this file:
os.chdir(os.path.dirname(__file__))

# Tell pyrosim where to save the geometry:
pyrosim.Start_SDF("tower.sdf")

# Create a tower of boxes such that the bottom cube is 1m^3 and each
# subsequent cube has 90% of the volume of the previous cube

# Define a function to create a tower of cubes:

def create_tower(basePos=[0,0,0],nCubes=10,sideLength=1):
    # Initiate base position, side length, and cube-center height variables:
    bx, by, bz = basePos
    side=sideLength
    height=side/2 # center of the bottom box
    for i in range(nCubes):
        pyrosim.Send_Cube(
            name=f"Box_{bx}_{by}_{i}",
            pos=[bx, by, height],
            size=[side, side, side])
        height += side/2 # Move to the top of current cube
        side*=0.9 # Shrink for next cube
        height+=side/2 # Move to the center of next cube

# Create a tower:
# create_tower(basePos=[0,0,0],nCubes=9)

# Create a grid of towers:
for i in range(5):
    for j in range(5):
        create_tower(basePos=[i,j,0],nCubes=10,sideLength=1)

# Close the SDF file and write it to disk:
pyrosim.End()