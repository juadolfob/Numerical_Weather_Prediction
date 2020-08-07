"""
wind

M : speed()
α : direction()

"""
from math import atan2, pi, degrees, sin, cos

class wind:
    """
    wind
    """

    @staticmethod
    def speed(u, v):
        """
        :return speed
        """
        M = (u ** 2 + v ** 2) ** (1 / 2)
        return M

    @staticmethod
    def direction(u, v):
        """
        :return angle in radians
        """
        a0 = 0
        if u > 0:
            a0 = pi
        return 1 / 2 * pi - atan2(v, u) + a0

    @staticmethod
    def velocity_components(degree, M):
        """
        :return u,v components
        """
        u = -M * sin(degree)
        v = -M * cos(degree)
        return u, v


class cylindrical_coordinates:
    """
     cylindrical coordinates(M, a, W)
     M : speed
     a : azimuth angle
     W : vertical velocity
    """

    def __init__(self, speed, angle, w):
        # M
        self.speed = speed
        # a
        self.angle = angle
        # W
        self.w = w


class cartesian_coordinates:
    """
     Cartesian (u, v, w)
     u : u velocity
     v : v velocity
     w : vertical velocity
    """

    def __init__(self, u, v, w):
        # u
        self.u = u
        # v
        self.v = v
        # w
        self.w = w
