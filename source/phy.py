from source.pf import f
import numpy as np


class p_object:

    def __init__(self, mass=1, velocity=None, position=None):
        # Mass
        self.M = mass
        # Velocity
        if velocity is not None:
            self.velocity = velocity
        else:
            self.velocity = np.array([0, 0, 0])
        # Position
        if position is not None:
            self.velocity = position
        else:
            self.position = np.array([0, 0, 0])


a = p_object(10, np.array([1, 1, 1]))

for i in range(0, 100, 1):
    print(f.delta_position(a.position, a.velocity, i))
