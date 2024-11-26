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
```plaintext
drone-simulation-project/
├── src/                            # Core source code
│   ├── models/                     # Drone models
│   │   ├── aerodynamics.py         # Aerodynamic calculations
│   │   ├── dynamics.py             # Equations of motion
│   │   ├── sensors.py              # Sensor simulation
│   │   └── control.py              # Control system (e.g., PID)
│   ├── simulations/                # Simulation scripts
│   │   ├── hover_simulation.py     # Hovering stability simulation
│   │   ├── flight_simulation.py    # Forward flight and disturbances
│   │   └── validate_model.py       # Model validation
│   └── utils/                      # Utility functions
│       ├── plotting.py             # Visualization tools
│       ├── helpers.py              # Helper functions
│       └── constants.py            # Constants like air density, gravity, etc.
├── tests/                          # Unit tests
│   ├── test_aerodynamics.py        # Tests for aerodynamics calculations
│   ├── test_dynamics.py            # Tests for equations of motion
│   └── test_control.py             # Tests for control systems
├── data/                           # Input/output data
│   ├── raw/                        # Raw input data
│   └── processed/                  # Processed or simulation output files
├── notebooks/                      # Jupyter notebooks for prototyping
│   ├── aerodynamics_analysis.ipynb
│   ├── control_testing.ipynb
│   └── flight_dynamics.ipynb
├── docs/                           # Documentation and resources
│   ├── requirements.md             # Details of project requirements
│   ├── design_process.md           # Description of design goals and steps
│   └── references.md               # Links or PDFs of referenced materials
├── .gitignore                      # Files to ignore in Git
├── README.md                       # Project overview
├── requirements.txt                # Required Python libraries
├── LICENSE                         # Project license
└── setup.py                        # Script for installing the project
```

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

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Run a Sample Simulation**:
    ```bash
    python src/simulations/hover_simulation.py

---

## Usage
- **Run Simulations**: 
    - Hovering: Analyze stability during stationary flight
    - Forward Flight: Measure energy efficiency and range
    - Disturbances: Test drone responses to wind gusts and payload shifts
- **Customize the Model**:
    - Modify src/models/dynamics.py to adjust drone geometry or physical parameters
    - Update src/models/control.py to tune PID gains
- **Visualize Results**:
    - Use Matplotlib/Plotly scripts in src/utils/plotting.py to generate graphs

---

## Performance Metrics
The project evaluates the drone's performance using the following metrics:
- **Stability**: Angular deviations in roll, pitch, and yaw
- **Energy Efficiency**: Power consumption during various flight scenarios
- **Range and Endurance**: Maximum distance and flight time
- **Disturbance Rejection**: Recovery time from wind gusts or payload shifts

---

## Future Goals
- Integrate advanced sensor models like cameras and LiDAR for object tracking
- Add environmental factors like turbulence and temperature variations
- Expand the simulation to include payloads and dynamic center of mass shifts
- Implement hardware-in-the-loop (HIL) testing with a physical drone

---

## License
This project is licensed under the MIT License

---

## Acknowledgments
- Python-Control: For control system design and simulation
- PyBullet: For physics-based simulations
- Matplotlib: For plotting results
- SciPy: For solving equations of motion

---


