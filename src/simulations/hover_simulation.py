"""
This script simulates hover by applying equal thrust on all motors
"""

import numpy as np
from src.models.control import PIDController
from src.models.dynamics import translational_motion
from src.utils.constants import DRONE_MASS, GRAVITY


# Initialize parameters
dt = 0.01  # Time step
time = np.arange(0, 20, dt) 
target_altitude = 10.0  # Desired altitude (m)
current_altitude = 0.0
velocity = 0.0

# Initialize PID controller
pid = PIDController(kp=2.0, ki=0.5, kd=0.1)

# Simulation loop
altitudes = []
for t in time:
    thrust = pid.update(target_altitude, current_altitude, dt)
    forces = [0.0, 0.0, float(thrust - DRONE_MASS * GRAVITY)]  # Forces in x, y, z
    # print(f"Forces at time {t}: {forces}")  # Debug forces
    position, velocity = translational_motion(forces, current_altitude, velocity, dt)
    current_altitude = position  
    altitudes.append(current_altitude)

# Plot results
import matplotlib.pyplot as plt
plt.plot(time, altitudes)
plt.title("Hover Stability")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid()
plt.show()
