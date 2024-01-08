import math
import matplotlib.pyplot as plt
import numpy as np


class Disc:
    gravitation = 9.81  # Accélération due à la gravité

    def __init__(self, speed0, degree0):
        self.speed0 = speed0
        self.degree0 = degree0

    def calculate_trajectory(self):
        theta_rad = self.__degree_to_rad()
        t_flight = self.__trajectory_time()

        #tables
        t = np.linspace(0, t_flight, num=1000)  # Discrétisation du temps
        x = self.speed0 * math.cos(theta_rad) * t
        y = self.speed0 * math.sin(theta_rad) * t - 0.5 * self.gravitation * t ** 2
        speed_y = np.sqrt(self.speed0 ** 2 - 2 * self.gravitation * y)

        # Calcul de la portée maximale, du temps de vol et de la hauteur maximale
        R = self.__horizontal_maximum(theta_rad)
        H = self.__vertical_maximum(theta_rad)

        return x, y, speed_y, R, t_flight, H, t

    def flight_time

    def __horizontal_maximum(self, theta_rad):
        return self.speed0 ** 2 * math.sin(2 * theta_rad) / self.gravitation

    def __vertical_maximum(self, theta_rad):
        return (self.speed0 ** 2 * math.sin(theta_rad) ** 2) / (2 * self.gravitation)

    # Conversion degrés à radians
    def __degree_to_rad(self):
        return math.radians(self.degree0)

    # Calcul des composantes x et y de la trajectoire
    def __trajectory_time(self):
        return 2 * self.speed0 * math.sin(self.__degree_to_rad()) / self.gravitation
