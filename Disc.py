import math
import matplotlib.pyplot as plt
import numpy as np


class Disc:
    gravitation = 9.81  # Accélération due à la gravité

    def __init__(self, speed0, degree0):
        self.speed0 = speed0
        self.degree0 = degree0
        self.__theta_rad = self.__degree_to_rad()
        self.__time_flight = self.__trajectory_time()

    def calculate_trajectory(self):
        t = np.linspace(0, self.__time_flight, num=1000)  # Discrétisation du temps
        x = self.speed0 * math.cos(self.__theta_rad) * t
        y = self.speed0 * math.sin(self.__theta_rad) * t - 0.5 * self.gravitation * t ** 2

        return x, y

    def get_fight_time(self):
        return self.__time_flight

    def get_speed_y(self):
        return np.sqrt(self.speed0 ** 2 - 2 * self.gravitation * y)
    def get_horizontal_maximum(self):
        return self.speed0 ** 2 * math.sin(2 * self.__theta_rad) / self.gravitation

    def get_vertical_maximum(self):
        return (self.speed0 ** 2 * math.sin(self.__theta_rad) ** 2) / (2 * self.gravitation)

    # Conversion degrés à radians
    def __degree_to_rad(self):
        return math.radians(self.degree0)

    # Calcul des composantes x et y de la trajectoire
    def __trajectory_time(self):
        return 2 * self.speed0 * math.sin(self.__degree_to_rad()) / self.gravitation
