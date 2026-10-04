import numpy as np
import matplotlib.pyplot as plt

# Load sensor data
backLegSensorValues=np.load("data/results/backLegSensorValues.npy")
frontLegSensorValues=np.load("data/results/frontLegSensorValues.npy")

# Plot the sensor data
plt.plot(backLegSensorValues,linewidth=3,label='back leg')
plt.plot(frontLegSensorValues,label='front leg')
plt.legend()
plt.show()