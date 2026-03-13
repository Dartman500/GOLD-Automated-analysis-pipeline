"""
GOLD satellite data reader
Extracts radiance and coordinates from GOLD NetCDF files
"""

import numpy as np
from netCDF4 import Dataset


def load_gold_file(filename):
    """
    Load GOLD NetCDF file.

    Parameters
    ----------
    filename : str
        Path to GOLD NetCDF file

    Returns
    -------
    lat : ndarray
    lon : ndarray
    wavelength : ndarray
    radiance : ndarray
    """

    with Dataset(filename, "r") as g:

        wavelength = g.variables["WAVELENGTH"][:]
        lat = g.variables["REFERENCE_POINT_LAT"][:]
        lon = g.variables["REFERENCE_POINT_LON"][:]
        radiance = g.variables["RADIANCE"][:]

    return lat, lon, wavelength, radiance
