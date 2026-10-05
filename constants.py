import numpy as np

# 1. Simulation Parameters: #

# Simulation duration (ticks):
simDuration = 10000
# Frame duration (in seconds):
frameDuration = 1/2000#1/240

# Motor parameters:
frontLegAmplitude=np.pi/4
frontLegFrequency=100
frontLegPhaseOffset=0
backLegAmplitude=np.pi/4
backLegFrequency=50
backLegPhaseOffset=np.pi/2