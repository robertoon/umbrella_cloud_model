from __future__ import division
import numpy as np
from scipy.stats import norm
from math import exp, pi, cos, sin, radians
from src.config import *
from src.utils import polar2cartesian, particle_diameter

# GENERATE PHI CLASSES
phis = np.arange(MAX_PHI, MIN_PHI + STEP_PHI, STEP_PHI)
PHI_CLASSES = [float(round(phi, 1)) for phi in phis]

# CALCULATE WIND VECTOR COMPONENTS (u, v)
U_WIND = WIND_SPEED * cos(radians(polar2cartesian(WIND_DIRECTION)))
V_WIND = WIND_SPEED * sin(radians(polar2cartesian(WIND_DIRECTION)))


def particle_density(phi):
    '''calculate particle density for given phi class'''
    max_grainsize = min(PHI_CLASSES)
    min_grainsize = max(PHI_CLASSES)

    if phi < max_grainsize:
        return PARTICLE_DENSITY_MIN
    elif phi >= max_grainsize and phi < min_grainsize:
        num = (PARTICLE_DENSITY_MAX - PARTICLE_DENSITY_MIN) * \
            (phi - min_grainsize)
        denom = max_grainsize - min_grainsize
        return PARTICLE_DENSITY_MAX - (num / denom)
    else:
        return PARTICLE_DENSITY_MAX


def mass_fraction(phi):
    '''calculate the mass fraction of each phi class'''
    P1 = norm.cdf(phi, TGSD_MEAN, TGSD_SIGMA)
    P2 = norm.cdf(phi + STEP_PHI, TGSD_MEAN, TGSD_SIGMA)
    return P2 - P1


def settling_velocity(phi):
    '''calculate settling velocity for each phi class'''
    v_aux = 0

    for atm_layer in range(ATMOSPHERE_LEVEL_STEP, COLUMN_HEIGHT + ATMOSPHERE_LEVEL_STEP, ATMOSPHERE_LEVEL_STEP):
        v_layer = 0

        elev = COLUMN_HEIGHT - atm_layer
        rho_a = RHO_A_S * exp(-1 * elev / 8200)
        rho = particle_density(phi) - rho_a

        v_l = (G * particle_diameter(phi)**2 * rho) / (18 * AIR_VISC)
        v_i = particle_diameter(
            phi) * ((4 * G**2 * rho**2) / (225 * AIR_VISC * rho_a))**(1/3)
        v_t = ((3.1 * rho * G * particle_diameter(phi))/(rho_a))**0.5

        re_l = (particle_diameter(phi) * rho_a * v_l) / AIR_VISC
        re_i = (particle_diameter(phi) * rho_a * v_i) / AIR_VISC
        re_t = (particle_diameter(phi) * rho_a * v_t) / AIR_VISC

        if re_l < 6:
            v_layer = v_l

        elif re_t >= 500:
            v_layer = v_t

        else:
            v_layer = v_i

        if v_layer == v_aux:
            return v_layer
        else:
            v_aux = v_layer

    return v_layer


def get_setling_velocities():
    '''return a dictionary with settling velocities for each phi class'''
    return {phi: settling_velocity(phi) for phi in PHI_CLASSES}


def get_particle_mass_fractions():
    '''return a dictionary with mass fractions for each phi class'''
    particle_mass_fractions = {}
    sum_mass_fraction = 0
    for phi in PHI_CLASSES:
        particle_mass_fractions[phi] = mass_fraction(phi)
        sum_mass_fraction += particle_mass_fractions[phi]

    # sum of all particle_mass_fractions should be 1
    # we divide the mass fraction error to each phi class
    mass_fraction_error = 1 - sum_mass_fraction
    if mass_fraction_error > 0:
        mass_fraction_error_unit = mass_fraction_error / len(PHI_CLASSES)
        for phi in PHI_CLASSES:
            particle_mass_fractions[phi] += mass_fraction_error_unit
    # in this point, sum of all particle_mass_fractions should be 1

    return particle_mass_fractions


def tephra_load(x, y, disk_cell_x, disk_cell_y, mass, velocity):
    '''calculate tephra accumulation at given (x, y) location
    '''
    source_term = (velocity * mass) / (4 * pi * COLUMN_HEIGHT * DIFFUSION_COEF)
    denom = 4 * DIFFUSION_COEF * (COLUMN_HEIGHT/velocity)
    advection = (x - (disk_cell_x + U_WIND *
                      COLUMN_HEIGHT / velocity))**2 / denom
    diffusion = (y - (disk_cell_y + V_WIND *
                      COLUMN_HEIGHT / velocity))**2 / denom

    return source_term * exp(-advection - diffusion)
