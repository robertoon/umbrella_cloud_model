import numpy as np
from math import sqrt, cos, sin, radians
from src.tephra import mass_fraction, particle_density
from src.utils import distance_between_points, polar2cartesian
from src.config import (
    CUSTOM_POINTS_FILE,
    GROUND_GRID_SIZE,
    DISPERSAL_AXIS_POINTS_DISTANCE,
    DISPERSAL_AXIS_POINTS_NUMBER
)


def generate_disk_grid(center_x, center_y, grid_step, disk_radius):
    '''
    Defining the umbrella cloud:
    1) generate equidistant points in the square enclosing the disk using a grid step
    2) keep only the points enclosed by disk radius
    '''
    grid_cells = []
    #center_x = center_x + 5000  # displacement on (0,x) axis

    for i in range(grid_step, 2 * disk_radius + grid_step, grid_step):
        for j in range(grid_step, 2 * disk_radius + grid_step, grid_step):
            grid_cell = {
                'x': center_x - disk_radius + i - grid_step/2,
                'y': center_y - disk_radius + j - grid_step/2
            }

            if distance_between_points(grid_cell['x'], grid_cell['y'], center_x, center_y) <= disk_radius:
                grid_cells.append(grid_cell)

    return grid_cells


def generate_ground_grid(min_x, max_x, min_y, max_y):
    '''generate the ground grid on which tephra load is calculated'''
    step = int((max_x - min_x) / sqrt(GROUND_GRID_SIZE))

    return (
        {'x': x, 'y': y}
        for x in range(min_x, max_x, step)
        for y in range(min_y, max_y, step)
    )


def get_custom_points():
    '''
    read (x y) points from input file of locations of interest
    for tephra load calculation
    '''
    point_x, point_y = np.genfromtxt(CUSTOM_POINTS_FILE, unpack=True)

    return (
        {'x': x, 'y': y} for x, y in zip(point_x, point_y)
    )


def get_dispersal_axis_points(x_vent, y_vent, alpha):
    '''
    define a series of points along the dispersal axis to
    calculate tephra accumulation
    '''
    alpha = polar2cartesian(alpha)
    points = []
    for i in range(DISPERSAL_AXIS_POINTS_NUMBER):
        distance = DISPERSAL_AXIS_POINTS_DISTANCE * (i + 1)
        x = x_vent + (distance * cos(radians(alpha)))
        y = y_vent + (distance * sin(radians(alpha)))
        points.append({'x': x, 'y': y})
    return points
