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

# Initiate side and height variables:
side=1
height=side/2 # center of the bottom box

# Loop to create a tower of cubes:
for i in range(9):
    pyrosim.Send_Cube(
        name=f"Box{i}",
        pos=[0, 0, height],
        size=[side, side, side])
    height += side/2 # Move to the top of current cube
    side*=0.9 # Shrink for next cube
    height+=side/2 # Move to the center of next cube

# Close the SDF file and write it to disk:
pyrosim.End()