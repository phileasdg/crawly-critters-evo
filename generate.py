import pyrosim.pyrosim as pyrosim

# Tell pyrosim where information about the world should be stored:
pyrosim.Start_SDF("box.sdf")

# Create a 1m^3 box resting at (x=0, y=0, z=0.5) (i.e. on the ground):
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])

# Close the SDF file and write it to disk:
pyrosim.End()