"""
This file stabilizes the drone in hover using a PID controller
"""

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0.0  
        self.integral = 0.0     

    def update(self, target, actual, dt):
        """
        Calculates control output based on PID
        """
        error = float(target - actual) 
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return float(output) 