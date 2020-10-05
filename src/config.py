'''
Configuration file for pyTephra2_uc code with umbrella cloud geometry.
All units are in international system units (i.e. kilograms, meters,
meters per second, kilograms per square meter).

'''

# SELECT RUN MODE: - DEFAULT VALUES ARE 'grid', 'custom points' OR 'dispersal axis points'
RUN_MODE = "custom points"

OUTPUT_FILE_NAME = "output.txt"  # writes (x, y, thickness) data

# INPUT FILE FOR 'CUSTOM POINTS' RUN MODE (e.g. must contain (x, y) data)
CUSTOM_POINTS_FILE = "custom_x_y_pulu.txt"

# MAP AREA AND VENT COORDINATES
MIN_EASTING = -50000
MAX_EASTING = 50000
MIN_NORTHING = -50000
MAX_NORTHING = 50000
VENT_EASTING = 0
VENT_NORTHING = 0

# GROUND GRID RESOLUTION (DEFAULT MAP HAS 1000 GRID CELLS)
GROUND_GRID_SIZE = 100**2

# UMBRELLA CLOUD GEOMETRY PARAMETERS
DISK_RADIUS = 12000
DISK_GRID_STEP = 1000

# ERUPTION PARAMETERS
TOTAL_ERUPTED_MASS = 2.5e+11
COLUMN_HEIGHT = 25000
BULK_DENSITY = 1000  # bulk density of the tephra deposit
PARTICLE_DENSITY_MAX = 1000  # deposit density range
PARTICLE_DENSITY_MIN = 1000
DIFFUSION_COEF = 9500  # in m^2 s^-1
WIND_SPEED = 0
WIND_DIRECTION = 0     # downwind direction in degrees from N


# DEFINE PHI INTERVALS (min | max phi according to TGSD)
MAX_PHI = -7
MIN_PHI = 11
# TGSD_SIGMA = 1.687
# TGSD_MEAN = -2.398
TGSD_SIGMA = 2.31
TGSD_MEAN = 0.82

# SIMULATED PHI INTERVALS (phi interval to be simulated)
SIMULATED_MAX_PHI = -7
SIMULATED_MIN_PHI = 11
STEP_PHI = 1

# CONSTANTS FOR SETTLING VELOCITY CALCULATION
ATMOSPHERE_LEVEL_STEP = 500  # 500 m thick atmosphere slices
RHO_A_S = 1.225              # density at sea level
G = 9.81                     # gravitational constant
AIR_VISC = 1.8325e-5         # air viscosity in N s / m^2 at 24C
ETA = 1                      # unitless

# DEFINE THE DISPERSAL AXIS RESOLUTION
DISPERSAL_AXIS_POINTS_NUMBER = 500    # total number of points
DISPERSAL_AXIS_POINTS_DISTANCE = 100  # distance between two points
