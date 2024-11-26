"""
This file models the drone's translational and rotational motion
"""

import numpy as np
from src.utils.constants import DRONE_MASS


def translational_motion(forces, initial_position, initial_velocity, time_step=0.01):
    """
    Models translational motion (z-axis in this case).
    forces: [F_x, F_y, F_z] in Newtons
    """
    # Flatten and ensure forces are numeric
    forces = np.array([float(f) for f in forces], dtype=float)

    # Calculate acceleration, velocity, and position for the z-axis
    acceleration = forces[2] / DRONE_MASS  # Use only the z-component
    velocity = initial_velocity + acceleration * time_step
    position = initial_position + velocity * time_step

    return position, velocity


def rotational_motion(torques, inertia, initial_angle, initial_angular_velocity, time_step=0.01):
    """
    Models rotational motion (roll, pitch, yaw)
    """
    angular_acceleration = np.array(torques) / inertia
    angular_velocity = initial_angular_velocity + angular_acceleration * time_step
    angle = initial_angle + angular_velocity * time_step
    return angle, angular_velocity

