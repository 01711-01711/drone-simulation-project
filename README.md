# Malicious Drone Interception Simulation Project

## Project Overview
This project focuses on simulating an interceptor drone's dynamics, aerodynamics, and control systems using Python. 
The simulation aims to model key flight behaviors such as hovering, forward flight, and responses to environmental disturbances, 
laying the groundwork for advanced drone design and functionality in future iterations.

---

## Features
- **Aerodynamics Modelling**: Simulates lift, drag, and thrust forces based on drone geometry and environmental factors
- **Flight Dynamics**: Models the equations of motion (translational and rotational) for a quadcopter
- **Control Systems**: Implements PID controllers to stabilize roll, pitch, yaw, and altitude
- **Sensor Simulation**: Simulates onboard sensors like IMU, GPS, and LiDAR for tracking and stability
- **Performance Analysis**: Measures key metrics like stability, energy efficiency, range, and power consumption
- **Visualization**: 2D/3D plots to visualize flight paths, stability margins, and performance indices

---

## Project Structure
drone-simulation-project/ ├── src/ # Core source code │ ├── models/ # Drone models │ │ ├── aerodynamics.py # Aerodynamic calculations │ │ ├── dynamics.py # Equations of motion │ │ ├── sensors.py # Sensor simulation │ │ └── control.py # Control system (e.g., PID) │ ├── simulations/ # Simulation scripts │ │ ├── hover_simulation.py # Hovering stability simulation │ │ ├── flight_simulation.py# Forward flight and disturbances │ │ └── validate_model.py # Model validation │ └── utils/ # Utility functions ├── tests/ # Unit tests ├── data/ # Input/output data ├── notebooks/ # Jupyter notebooks for prototyping ├── docs/ # Documentation and references ├── .gitignore # Files to ignore in Git ├── README.md # Project overview ├── requirements.txt # Required Python libraries └── setup.py # Install script

---

## Installation
To set up the project on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/01711-01711/drone-simulation-project.git
   cd drone-simulation-project

2. **Set Up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows

---

