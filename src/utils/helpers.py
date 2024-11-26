"""
This file contains reusable helper functions (e.g., unit conversions)
"""

from utils.constants import AIR_DENSITY


def thrust_to_power(thrust, efficiency=0.8):
    """
    Converts thrust (N) to power required (W) using efficiency
    """
    return thrust / efficiency

def drag_force(velocity, drag_coefficient, area):
    """
    Calculates drag force based on velocity, drag coefficient, and area
    """
    return 0.5 * AIR_DENSITY * drag_coefficient * area * velocity**2


