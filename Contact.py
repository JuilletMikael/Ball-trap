import math
import matplotlib.pyplot as plt
import numpy as np


class Contact(object):

    def __init__(self, bullet) :
        self.bullet = bullet
        self.__touch_time = 0
        self.__wait_time = 0
        self.double = []

    def get_double(self):
        return self.double

    def get_wait_time(self):
        return self.__wait_time

    def get_touch_time(self):
        return self.__touch_time

    # if contact is double return double value and show two points (maybe render differently)
    # if one contact show intersection one
    # if none dont show intesection
    def contact(self):
        t1, w1, t2, w2 = self.time_and_wait()

        if (self.bullet.x0 < 0 or self.bullet.x0 > 500) :
            self.double = [t1, w1, t2, w2]

        else:
            if (self.bullet.degree0 >= 90):
                # TODO : Fix 90 degree
                self.__touch_time, self.__wait_time = self.min(t1, w1, t2, w2)

            if (self.bullet.degree0 < 90):
                self.__touch_time, self.__wait_time = self.max(t1, w1, t2, w2)

    def max(self, t1, w1, t2, w2):

        if (t1 > t2):
            return t1, w1
        else:
            return t2, w2

    def min(self, t1, w1, t2, w2):

        if (t1 < t2):
            return t1, w1
        else:
            return t2, w2

    def time_and_wait(self):
        t1 = ((0.45152364098575 * (abs(math.cos(math.radians(self.bullet.degree0)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(self.bullet.degree0)) * math.cos(
                math.radians(self.bullet.degree0)) * self.bullet.x0 + 124.87257900102 * (
                    math.cos(math.radians(self.bullet.degree0)) - math.sin(math.radians(self.bullet.degree0))) ** (
                2)) + 11.174639994247 * ((math.cos(math.radians(self.bullet.degree0))) ** (2) - (
                math.sin(math.radians(self.bullet.degree0)) + 0.41247895569216) * math.cos(
            math.radians(self.bullet.degree0)) + 0.41247895569215 * math.sin(math.radians(self.bullet.degree0))))) / (
                      math.cos(math.radians(self.bullet.degree0)) * (
                      math.cos(math.radians(self.bullet.degree0)) - 0.41247895569216)))
        w1 = ((0.45152364098573 * (abs(math.cos(math.radians(self.bullet.degree0)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(self.bullet.degree0)) * math.cos(
                math.radians(self.bullet.degree0)) * self.bullet.x0 + 124.87257900102 * (
                    math.cos(math.radians(self.bullet.degree0)) - math.sin(math.radians(self.bullet.degree0))) ** (
                2)) + 0.018456028825292 * (math.cos(math.radians(self.bullet.degree0)) * self.bullet.x0 + 605.47369642885 * (
                (math.cos(math.radians(self.bullet.degree0))) ** (2) - (
                math.sin(math.radians(self.bullet.degree0)) + 0.41247895569216) * math.cos(
            math.radians(self.bullet.degree0)) + 0.41247895569215 * math.sin(math.radians(self.bullet.degree0)))))) / (
                      (math.cos(math.radians(self.bullet.degree0))) ** (2)))

        t2 = ((-0.45152364098575 * (abs(math.cos(math.radians(self.bullet.degree0)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(self.bullet.degree0)) * math.cos(
                math.radians(self.bullet.degree0)) * self.bullet.x0 + 124.87257900102 * (
                    math.cos(math.radians(self.bullet.degree0)) - math.sin(math.radians(self.bullet.degree0))) ** (
                2)) - 11.174639994247 * ((math.cos(math.radians(self.bullet.degree0))) ** (2) - (
                math.sin(math.radians(self.bullet.degree0)) + 0.41247895569216) * math.cos(
            math.radians(self.bullet.degree0)) + 0.41247895569215 * math.sin(math.radians(self.bullet.degree0))))) / (
                      math.cos(math.radians(self.bullet.degree0)) * (
                      math.cos(math.radians(self.bullet.degree0)) - 0.41247895569216)))
        w2 = ((-0.45152364098573 * (abs(math.cos(math.radians(self.bullet.degree0)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(self.bullet.degree0)) * math.cos(
                math.radians(self.bullet.degree0)) * self.bullet.x0 + 124.87257900102 * (
                    math.cos(math.radians(self.bullet.degree0)) - math.sin(math.radians(self.bullet.degree0))) ** (
                2)) - 0.018456028825292 * (math.cos(math.radians(self.bullet.degree0)) * self.bullet.x0 + 605.47369642885 * (
                (math.cos(math.radians(self.bullet.degree0))) ** (2) - (
                math.sin(math.radians(self.bullet.degree0)) + 0.41247895569216) * math.cos(
            math.radians(self.bullet.degree0)) + 0.41247895569215 * math.sin(math.radians(self.bullet.degree0)))))) / (
                      (math.cos(math.radians(self.bullet.degree0))) ** 2))

        return t1, w1, t2, w2

