import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))

# # Load sensor data
backLegSensorValues=np.load("data/results/backLegSensorValues.npy")
frontLegSensorValues=np.load("data/results/frontLegSensorValues.npy")

# Plot the sensor data
plt.plot(backLegSensorValues,linewidth=3,label='back leg')
plt.plot(frontLegSensorValues,label='front leg')
plt.legend()
plt.show()

# Load target angles
frontLegTargetAngles=np.load("data/results/frontLegTargetAngles.npy")
backLegTargetAngles=np.load("data/results/backLegTargetAngles.npy")

# Plot the target angles
plt.plot(frontLegTargetAngles,linewidth=2,label='Front leg motor values')
plt.plot(backLegTargetAngles,label='Back leg motor values')
plt.legend()
plt.show()