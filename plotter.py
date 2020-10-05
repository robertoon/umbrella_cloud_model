import numpy as np
import matplotlib.pyplot as plt
from src.config import (
    VENT_EASTING,
    VENT_NORTHING)
from src.utils import (distance_between_points)

# PLOT THICKNESS VS DISTANCE ON DISPERSAL AXIS ############

X = []
Z = []
x, y, z = np.genfromtxt(r'./output_test1.txt', unpack=True)
for idx, lon in enumerate(x):
    X.append(distance_between_points(VENT_EASTING, VENT_NORTHING, lon, y[idx]))
    Z.append(z[idx])

plt.plot(X, Z, color='tab:red', linestyle='--', linewidth=1.4, label="Sim data")

###############################################################################################
plt.axvline(
      x=9000,  color='black',
      linestyle='--', linewidth=0.4
)
plt.axis([min(X), max(X), 0, 50], aspect="auto")
plt.text(36000, 20, 'Mass = 0.5e11kg\nRadius = 9km\nHeight = 14km\nK = 6000\nWind = 10m/s\nD=225')
plt.xlabel('Distance $(m)$')
plt.ylabel('Thickness $(cm)$')
plt.legend(facecolor='ghostwhite')
plt.show()
