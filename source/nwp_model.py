
"""

"""
from math import cos, degrees, radians

from source.constants import earth, universal as u


def radial_distance(latitude=0, longitud=None):
    """
    return equatorial radius if no arguments are passed

    :return: earth_radius
    """
    return earth.volumetric_mean_radius_km


def geopotential(height, latitud):
    """
    Geopotential: Product of height z by acceleration due to gravity g, which combines only the effects of Newtonian gravity g* and the centrifugal force
    expressed in J.kg−1 in SI units.

    g : surface_gravity_m_s2
    z : height
    r : radial distance

    :return:
    """
    g = u.newtonian_gravitational_constant
    z = height
    r = earth.equatorial_radius_km
    Om = earth.angular_velocity
    _geopotential = g * z - (Om ** 2 * r ** 2 * cos(latitud) ** 2 / 2)
    return _geopotential


print(geopotential(10_000_000_000, radians(0)))


def momentum_equation():
    """
    -2 Ω
    :return:
    """
    -2


def angular_velocity_km_s(latitud):
    """

    :return:
    """
    v_equator = earth.equatorial_radius_km * earth.angular_velocity
    print(earth.equatorial_radius_km)
    print(earth.angular_velocity)
    print(cos(latitud))

    v_latitud = v_equator * cos(latitud)
    return v_latitud
