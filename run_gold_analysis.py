"""
Run GOLD ionosphere analysis pipeline
"""

from src.gold_reader import load_gold_file
from src.eia_extraction import extract_oxygen_1356
from src.plotting import plot_oxygen_map


def main():

    filename = "data/example_gold_file.nc"

    lat, lon, wavelength, radiance = load_gold_file(filename)

    oxygen_map = extract_oxygen_1356(wavelength, radiance)

    plot_oxygen_map(lat, lon, oxygen_map)


if __name__ == "__main__":
    main()
