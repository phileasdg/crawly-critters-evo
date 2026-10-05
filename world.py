import pybullet as p

class WORLD:
    def __init__(self):
        # Import geometry 
        # (a floor)
        self.planeId = p.loadURDF("plane.urdf")
        # (the world geometry)
        p.loadSDF("data/worlds/world.sdf")
        