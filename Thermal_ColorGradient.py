"""
Thermal Color Map Configuration File
Version: 1.0
Author: Gabriel S. Gutiérrez-Cárdenas
Created: 2025-03-30
License: Apache Liscense 2.0
Repository: https://github.com/Gabo2000s/Color_maps_ocean_atm
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Main color map definition
COLOR_DEFINITIONS = {
    "name": "Thermal_ColorGradient",
    "author": "Gabriel S. Gutiérrez-Cárdenas",
    "colors": [
        (0.0, (0.29, 0.0, 0.51)),      # #4B0082 (Deep Violet)
        (0.15, (0.48, 0.41, 0.93)),    # #7B68EE (Slate Blue)
        (0.3, (0.94, 0.97, 1.0)),      # #F0F8FF (Alice Blue)
        (0.45, (0.0, 0.42, 0.42)),     # #006D6D (Teal Green)
        (0.6, (0.20, 0.80, 0.20)),     # #32CD32 (Lime Green)
        (0.75, (1.0, 0.84, 0.0)),      # #FFD700 (Golden Yellow)
        (0.9, (1.0, 0.27, 0.0)),       # #FF4500 (Vermilion)
        (1.0, (0.55, 0.0, 0.0))        # #8B0000 (Dark Red)
    ],
    "metadata": {
        "classification": "diverging",
        "application": "temperature visualization",
        "perceptual_uniform": False
    }
}

def create_colormap(n_bins=256):
    """Creates and registers the colormap in Matplotlib
    
    Args:
        n_bins (int): Number of discrete segments for the gradient
    
    Returns:
        LinearSegmentedColormap: Configured colormap
    """
    return LinearSegmentedColormap.from_list(
        name=COLOR_DEFINITIONS["name"],
        colors=COLOR_DEFINITIONS["colors"],
        N=n_bins
    )

def register_colormap():
    """Registers the colormap in Matplotlib's system"""
    plt.register_cmap(name=COLOR_DEFINITIONS["name"], cmap=create_colormap())

def show_demo():
    """Displays a visual demonstration of the colormap"""
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack((gradient, gradient))
    
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.imshow(gradient, aspect="auto", cmap=create_colormap())
    ax.set_title(f"{COLOR_DEFINITIONS['name']} Colormap Demo\n"
                 f"Created by: {COLOR_DEFINITIONS['author']}",
                 fontsize=10)
    ax.set_axis_off()
    plt.show()

# Automatic registration on import
register_colormap()

if __name__ == "__main__":
    # Run demo when executed as script
    show_demo()