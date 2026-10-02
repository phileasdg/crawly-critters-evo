import os
import pyrosim.pyrosim as pyrosim

# Set the save path to be the folder containing this file:
os.chdir(os.path.dirname(__file__))

# Tell pyrosim where to save the geometry:
pyrosim.Start_SDF("boxes.sdf")

# Create a 1m^3 box resting at (x=0, y=0, z=0.5) (i.e. on the ground):
pyrosim.Send_Cube(name="Box1", pos=[0,0,.5] , size=[1,1,1]) # (Position is [x,y,z] and size is [length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1]) 
# Close the SDF file and write it to disk:
pyrosim.End()