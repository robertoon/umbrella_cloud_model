'''Utility functions to be used in specific calculations.'''
from math import sqrt


def distance_between_points(point1_x, point1_y, point2_x, point2_y):
    '''calculate distance between two points'''
    return sqrt((point2_x - point1_x)**2 + (point2_y - point1_y)**2)


def polar2cartesian(theta):
    '''convert polar to cartesian wind field data'''
    return (360 - theta + 90) % 360


def particle_diameter(phi):
    '''calculate particle diameter for given phi class'''
    return 2**(-1 * phi) * 10**-3
