



import numpy as np
from src.models.dynamics import translational_motion, rotational_motion
from src.models.control import PIDController
from src.utils.constants import DRONE_MASS, GRAVITY


# Initialize parameters
dt = 0.01
time = np.arange(0, 20, dt)

# Translational states
position = [0.0, 0.0, 0.0]
velocity = [0.0, 0.0, 0.0]
forces = [0.0, 0.0, 0.0]

# Rotational states
angles = [0.0, 0.0, 0.0]
angular_velocity = [0.0, 0.0, 0.0]
torques = [0.0, 0.0, 0.0]
inertia = [0.1, 0.1, 0.2]

# PID Controllers
altitude_pid = PIDController(kp=2.0, ki=0.5, kd=0.1)

# Simulation loop
altitudes = []
for t in time:
    # Translational dynamics
    forces[2] = altitude_pid.update(10.0, position[2], dt) - DRONE_MASS * GRAVITY
    position, velocity = translational_motion(forces, position, velocity, dt)

    # Rotational dynamics (assume torques are zero for now)
    angles, angular_velocity = rotational_motion(torques, inertia, angles, angular_velocity, dt)

    altitudes.append(position[2])

# Plot altitude results
import matplotlib.pyplot as plt
plt.plot(time, altitudes)
plt.title("6DOF Hover Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid()
plt.show()
