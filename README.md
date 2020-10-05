# pyTephra2_uc

Version: 0.10

Date: 12 September 2020

Coding and concept: Constantinescu R., Hopulele-Gligor A., Connor C.B.

Contact: Constantinescu R. - robertc1@usf.edu

# The code and the concept

The pyTephra2_uc code is used to simulate tephra sedimentation from umbrella clouds. The main equations are drawn from Tephra2 code, however, in this python version we switched from a subvertical plume geometry to a radial plume to simulate tephra sedimentation from umbrella clouds.
The config file allows the user to input the eruption source parameters (ESPs).
See requirements.txt to see the ncessary build environemnts.

The code calculates tephra thickness on a grid. There are three RUN MODES:
    'grid',
    'custom points'
    'dispersal axis points'

The 'grid' mode calculates tephra accumulation on the entire grid (map).
The 'custom points' calculates tephra accumulation at locations of interest (x,y) given an input file.
The 'dispersal axis points' calculates tephra accumulation at equally spaced points along the dispersal axis (i.e. wind direction).


# Running the code

To run the code you must be in the 'umbrella_cloud' directory.

Once the run mode is selected in the 'config.py' file, execute:

$python main.py

The plotter.py script is used to create a thickness vs distance plot from the outpufile of the main program. Edit the 'plotter.py' and change the 'field data'  and the 'thickness vs distance' files with the ones you need to plot. To run the plotter:

$python plotter.py

The 'equiline.py' script creates an equiline plot to visualize the fit between the modeled and observed thickness. Edit 'equiline.py' and change the input file. To run the program:

$equiline.py

# The config file

The config file is located in 'src' folder. Edit the config file to fill in the simulation parameters (eruption source parameters). An example is provided below:

1. Select the run mode:

RUN_MODE = "custom points" (alternatives are: 'grid' OR 'dispersal axis points')

2. Select outputfile name:
OUTPUT_FILE_NAME = "output.txt"  # writes (x, y, thickness data from the main program)

3. Select input file for with the custom points for the calculation (*not needed for 'grid' or 'dispersal axis points')
CUSTOM_POINTS_FILE = "custom_x_y_.txt" (e.g. must contain (x y) data)

4. Input the four corners of the map and vent location (in meters):
MIN_EASTING = -1
MAX_EASTING = 1
MIN_NORTHING = -1
MAX_NORTHING = 1
VENT_EASTING = 0.5
VENT_NORTHING = 0.5

5. Input ground grid resolution (default is 1000 equali spaced grid cells):
GROUND_GRID_SIZE = 100**2

6. Input the umbrella cloud dimensions (in meters) and the resolution for the grid defining the geometry:
DISK_RADIUS = 10000
DISK_GRID_STEP = 1000

7.  Input the rest of the eruption surce parameters (in S/I units: meters, kilograms):
TOTAL_ERUPTED_MASS = 2.5e+11
COLUMN_HEIGHT = 25000
BULK_DENSITY = 1000
PARTICLE_DENSITY_MAX = 1000
PARTICLE_DENSITY_MIN = 1000
DIFFUSION_COEF = 9500
WIND_SPEED = 0
WIND_DIRECTION = 0

8. Select the grain size classes of the deposit and the statistics:
MAX_PHI = -11
MIN_PHI = 11
TGSD_SIGMA = 0.31
TGSD_MEAN = 0.12

9. Select which grain size classes (from the total above) you wish to simulate and the phi class discretization:
SIMULATED_MAX_PHI = -1
SIMULATED_MIN_PHI = 3
STEP_PHI = 1

10. If simulating dispersal axis points, define the resolution:
DISPERSAL_AXIS_POINTS_NUMBER = 500
DISPERSAL_AXIS_POINTS_DISTANCE = 100



