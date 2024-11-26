"""
This file calculates forces like thrust and drag
"""

from src.utils.constants import AIR_DENSITY, PROP_DIAMETER, MAX_THRUST


def calculate_thrust(power, efficiency=0.8):
    """
    Calculates thrust from motor power and efficiency 
    """
    return power * efficiency / (PROP_DIAMETER ** 2)

def calculate_drag(velocity, drag_coefficient=0.3, cross_section_area=0.05):
    """
    Calculates drag force
    """
    return 0.5 * AIR_DENSITY * drag_coefficient * cross_section_area * velocity**2
