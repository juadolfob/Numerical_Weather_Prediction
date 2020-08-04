"""
NSEW
"""

nesw3 = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW "]
nesw2 = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
nesw = ["N", "E", "S", "W"]


def _normalize_degree(degree):
    return float(degree) % 360


def cardinal(degree):
    """
    converts a degree to an element of nesw
    ["N", "E", "S", "W"]


    :param degree: Meteorological degree
    :return: nesw cardinal direction
    """
    degree = _normalize_degree(degree)
    return nesw2[round((degree / 90)) % 4]  # 90 : 360/len(nesw); 4 : len(nesw)


def cardinal2(degree):
    """
    converts a degree to an element of nesw2
    ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


    :param degree: Meteorological degree
    :return: nesw2 cardinal direction
    """
    degree = _normalize_degree(degree)
    return nesw2[round((degree / 45)) % 8]  # 45 : 360/len(nesw2); 8 : len(nesw2)

def cardinal3(degree):
    """
    converts a degree to an element of nesw3
    ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW "]


    :param degree: Meteorological degree
    :return: nesw3 cardinal direction
    """
    degree = _normalize_degree(degree)
    return nesw3[round((degree / 22.5)) % 16]  # 22.5 : 360/len(nesw3); 16 : len(nesw3)
