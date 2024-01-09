import math
import matplotlib.pyplot as plt
import numpy as np

class Bullet(object):
    wait = 0
    x_overtime = []
    y_overtime = []

    def __init__(self, speed0, degree0, x0) :
        self.speed0 = speed0
        self.degree0 = degree0
        self.x0 = x0

    def calculate_trajectory(self, disc_fight_duration):
        # Conversion degrés à radians
        theta_rad_b = math.radians(self.degree0)

        t = np.linspace(0, disc_fight_duration, num=1000)  # Discrétisation du temps
        x = (self.speed0 * math.cos(theta_rad_b)) * (t - self.wait) + self.x0
        y = (self.speed0 * math.sin(theta_rad_b)) * (t - self.wait)

        return x, y

    def position_on_time(self, t):
        theta_rad_b = math.radians(self.degree0)

        return (self.speed0 * math.cos(theta_rad_b)) * (t - self.wait) + self.x0, (self.speed0 * math.sin(theta_rad_b)) * (t - self.wait)

    def set_wait(self, wait):
        self.wait = wait