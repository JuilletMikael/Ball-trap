import math
import matplotlib.pyplot as plt
import numpy as np

class Bullet(object):
    def __init__(self, speed0, degree0, x0, w) :
        self.speed0 = speed0
        self.degree0 = degree0
        self.x0 = x0
        self.w = w

    def calculate_trajectory(self, disc_fight_duration):
        # Conversion degrés à radians
        theta_rad_b = math.radians(self.degree0)

        # Composantes horizontale et verticale de la vitesse initiale
        v0_x = self.speed0 * math.cos(theta_rad_b)
        v0_y = self.speed0 * math.sin(theta_rad_b)

        t = np.linspace(0, disc_fight_duration, num=1000)  # Discrétisation du temps
        x = (self.speed0 * math.cos(theta_rad_b)) * (t - self.w) + self.x0
        y = (self.speed0 * math.sin(theta_rad_b)) * (t - self.w)

        return x, y, t

    def position_on_time(self, t):
        theta_rad_b = math.radians(self.degree0)

        return (self.speed0 * math.cos(theta_rad_b)) * (t - self.w) + self.x0, (self.speed0 * math.sin(theta_rad_b)) * (t - self.w)

