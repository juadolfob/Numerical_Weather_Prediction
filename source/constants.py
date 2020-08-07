"""
Earth's Bulk parameters
"""
import math


class universal:
    """
    universal constants
    """
    speed_of_light_m_s = 2.99792458e8
    newtonian_gravitational_constant = 6.67408e-11
    planck_constant = 6.626070040e-34
    # absolute_zero_celcius, not considered a true universal constant
    absolute_zero_celcius = -273.15


class earth:
    """
    earth constants
    """

    mass_kg = 5.9726e24
    earth_orbital_period_days = 365.256
    sidereal_day_hours = 23.9344696
    volumetric_mean_radius_km = 6371
    equatorial_radius_km = 6378.137
    polar_radius_km = 6356.752
    core_radius_km = 3485
    angular_velocity = 0.7292107e-4
    coriolis_factor = 2 * angular_velocity

    ellipticity = flattening = 0.003353
    mean_density_kg_m3 = 5514
    surface_gravity_m_s2 = 9.798
    surface_acceleration_m_s2 = 9.780
    escape_velocity_km_s = 11.186
    gm_km3_s2 = 0.39860e6
    bond_albedo = 0.306
    geometric_albedo = 0.434
    v_band_magnitude_V_1_0 = -3.99
    solar_irradiance_W_m2 = 1361.0
    black_body_temperature_K = 254.0
    topographic_range_km = 20.4
    moment_of_inertia_I_MR2 = 0.3308
    j2 = 1082.63e-6

    volume_km3 = 108.321e10
