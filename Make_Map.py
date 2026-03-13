"""
Plot GOLD ionosphere maps
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def plot_oxygen_map(lat, lon, oxygen_map):

    fig = plt.figure(figsize=(12, 8))

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    mesh = ax.pcolormesh(
        lon[9:-8, 9:-8],
        lat[9:-8, 9:-8],
        oxygen_map[9:-8, 9:-8].T,
        cmap="jet",
        vmin=5,
        vmax=15
    )

    ax.coastlines()
    ax.set_extent([-100, -20, -60, 60])

    cbar = fig.colorbar(mesh, orientation="horizontal", pad=0.05)
    cbar.set_label("135.6 nm Radiance")

    plt.title("GOLD Oxygen 135.6 nm Emission")
    plt.show()
