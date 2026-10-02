# Ludobots requirements:
import pybullet as p

# My own imports:
import time

# Connect to the physics sim GUI:
physicsClient = p.connect(p.GUI)

# Optional: disable the GUI sidebars:
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# Step the world:
for t in range(1000):
    print(f"t={t}")
    p.stepSimulation()
    time.sleep(1/60)
    
p.disconnect()