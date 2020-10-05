import sys
import time
import numpy as np
from math import sqrt
from src.config import *
from src.grids import (
    generate_disk_grid,
    generate_ground_grid,
    get_custom_points,
    get_dispersal_axis_points
)
from src.tephra import (
    PHI_CLASSES,
    mass_fraction,
    particle_density,
    settling_velocity,
    get_setling_velocities,
    get_particle_mass_fractions,
    tephra_load
)


start = time.time()

# DETECT THE TYPE OF SIMULATION AND USE NECESSARY PARAMETERS
# (e.g. full map (grid) or selected points (custom points or dispersal axis))
if RUN_MODE not in ['grid', 'custom points', 'dispersal axis points']:
    print('The RUN MODE must be <grid>, <custom points> or <dispersal axis points>')
    sys.exit()

if RUN_MODE == 'grid':
    ground_points = generate_ground_grid(
        MIN_EASTING, MAX_EASTING, MIN_NORTHING, MAX_NORTHING
    )

if RUN_MODE == 'custom points':
    ground_points = get_custom_points()

if RUN_MODE == 'dispersal axis points':
    ground_points = get_dispersal_axis_points(VENT_EASTING, VENT_NORTHING, WIND_DIRECTION)

# generate umbrella cloud grid as a function of vent coordinates,
# input radius and grid step
disk_grid = generate_disk_grid(
    VENT_EASTING, VENT_NORTHING, DISK_GRID_STEP, DISK_RADIUS
)

# generate phi classes to be simulated
simulated_phis = np.arange(SIMULATED_MAX_PHI, SIMULATED_MIN_PHI + STEP_PHI, STEP_PHI)
SIMULATED_PHI_CLASSES = [float(round(phi, 1)) for phi in simulated_phis]

# calculate settling_velocities and particle_mass_fractions for each phi
settling_velocities = get_setling_velocities()
particle_mass_fractions = get_particle_mass_fractions()

# calculate tephra load by integrating for each phi class from each disk cell
total_tephra_load = 0
disk_cells_count = len(disk_grid)
disk_cell_mass = TOTAL_ERUPTED_MASS / disk_cells_count
out = open(OUTPUT_FILE_NAME, 'w')

for ground_point in ground_points:
    total_load = 0

    for phi in SIMULATED_PHI_CLASSES:
        cell_mass = disk_cell_mass * particle_mass_fractions[phi]

        for disk_grid_cell in disk_grid:
            phi_load = tephra_load(
                ground_point['x'],
                ground_point['y'],
                disk_grid_cell['x'],
                disk_grid_cell['y'],
                cell_mass,
                settling_velocities[phi]
            )

            total_load += phi_load

    total_tephra_load += total_load
    tephra_tickeness = (total_load/BULK_DENSITY) * 100  # in cm
    out.write('%d %d %.6f\n' % (ground_point['x'], ground_point['y'], tephra_tickeness))
out.close()

# simulation messages
ground_grid_step = int((MAX_EASTING - MIN_EASTING) / sqrt(GROUND_GRID_SIZE))
print('Simulated phi classes: {}'.format(str(SIMULATED_PHI_CLASSES)))
print('Total erupted mass: {} kg'.format(TOTAL_ERUPTED_MASS))
print('Disk radius: {} m'.format(DISK_RADIUS))
print('Column height: {} m'.format(COLUMN_HEIGHT))
print('Disk grid resolution: {}x{} m'.format(DISK_GRID_STEP, DISK_GRID_STEP))
print('Disk grid cell count: {}'.format(len(disk_grid)))
print('Disk grid cell mass: {} kg'.format(disk_cell_mass))
print('Ground grid resolution: {}x{} m'.format(ground_grid_step, ground_grid_step))
print('Execution time: {:.2f} s'.format(time.time() - start))
print('Results are stored in: {}'.format(OUTPUT_FILE_NAME))
