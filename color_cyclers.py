import os
import numpy as np
from cycler import cycler

palette_csv = os.path.join(os.path.dirname(__file__), "color_palette.csv")
colors = np.genfromtxt(palette_csv, delimiter=",")

base_colors   = colors[:, 2]
blue_shades   = colors[0, :]
orange_shades = colors[1, :]
green_shades  = colors[2, :]
red_shades    = colors[3, :]
purple_shades = colors[4, :]
yellow_shades = colors[5, :]

ls_cycler = cycler("ls", ["-", "--", ".-", ":"])

base_color_cycler = cycler(color=base_colors) + ls_cycler
blue_shade_cycler = cycler(color=blue_shades)
orange_shade_cycler = cycler(color=orange_shades)
green_shade_cycler = cycler(color=green_shades)
red_shade_cycler = cycler(color=red_shades)
purple_shade_cycler = cycler(color=purple_shades)
yellow_shade_cycler = cycler(color=yellow_shades)


