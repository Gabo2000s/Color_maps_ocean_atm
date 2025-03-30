# Thermal ColorGradient Colormap 🌡️🎨

A custom Matplotlib diverging colormap for scientific visualization, optimized for temperature data representation. Hosted on GitHub for easy integration.

## Key Features
- **Smooth Transitions**: From deep violet (-20°C) to dark red (40°C)
- **One-Step Installation**: Direct GitHub integration
- **Version Control**: Always get the latest updates
- **Cross-Platform**: Works with any Python environment

## Installation & Setup

```python
import numpy as np
import matplotlib.pyplot as plt
import requests

# Register colormap from GitHub
url = "https://raw.githubusercontent.com/Gabo2000s/Color_maps_ocean_atm/main/Thermal_ColorGradient.py"
exec(requests.get(url).text)

# Verify registration
print("Available colormaps:", plt.colormaps()[-3:])  # Should show 'Thermal_ColorGradient'
```

## Basic Usage 

```python
# Generate sample data
data = np.linspace(-20, 40, 100).reshape(10, 10)

# Create plot
plt.imshow(data, cmap="Thermal_ColorGradient", vmin=-20, vmax=40)
cbar = plt.colorbar(label="Temperature (°C)")
plt.title("Thermal Distribution")
plt.show()
```
## Color Scheme
Position	RGB Values	Hex Code	Temperature
0.0	(0.29, 0.0, 0.51)	#4B0082	-20°C
0.3	(0.94, 0.97, 1.0)	#F0F8FF	5°C
0.6	(0.20, 0.80, 0.20)	#32CD32	20°C
1.0	(0.55, 0.0, 0.0)	#8B0000	40°C

## Best Practices
Set near vmin=-20 and vmax=40 for proper color scaling
Use dark backgrounds for optimal contrast
For publications:

```python
plt.rcParams['figure.dpi'] = 300  # High resolution
plt.rcParams['font.family'] = 'Serif'  # Academic style
```

## Compatibility
Tested with Matplotlib ≥ 3.8

Compatible with NumPy, Pandas, Xarray

Works in Jupyter notebooks and standalone scripts

## License
Apache 2.0 - Full details in LICENSE

Maintainer: Gabriel S. Gutiérrez-Cárdenas
Repository: https://github.com/Gabo2000s/Color_maps_ocean_atm
Issue Tracker: https://github.com/Gabo2000s/Color_maps_ocean_atm/issues
