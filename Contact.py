import math
import matplotlib.pyplot as plt
import numpy as np

class Contact(object):

    # if contact is double return double value and show two points (maybe render differently)
    # if one contact show intersection one
    # if none dont show intesection
    def x0_out(self):

        if (double()) :
            return

        if (degree0_bullet >= 90):
            # Adding 0.01 on 90 degree to avoid crash
            # TODO : Fix 90 degree
            if (degree0_bullet == 90):
                degree0_bullet = degree0_bullet + 0.001
            t, w = min()

        if (degree0_bullet < 90):
            t, w = max()


    # one contactshow intesection
    def x0_in(self):
        if (degree0_bullet >= 90):
            # Adding 0.01 on 90 degree to avoid crash
            # TODO : Fix 90 degree
            if (degree0_bullet == 90):
                degree0_bullet = degree0_bullet + 0.001
            t, w = min()

        if (degree0_bullet < 90):
            t, w = max()


    def max():
        t1 = ((0.45152364098575 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) + 11.174639994247 * ((math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet))))) / (
                      math.cos(math.radians(degree0_bullet)) * (
                      math.cos(math.radians(degree0_bullet)) - 0.41247895569216)))
        w1 = ((0.45152364098573 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) + 0.018456028825292 * (math.cos(math.radians(degree0_bullet)) * x0_bullet + 605.47369642885 * (
                (math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet)))))) / (
                      (math.cos(math.radians(degree0_bullet))) ** (2)))

        t2 = ((-0.45152364098575 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) - 11.174639994247 * ((math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet))))) / (
                      math.cos(math.radians(degree0_bullet)) * (
                      math.cos(math.radians(degree0_bullet)) - 0.41247895569216)))
        w2 = ((-0.45152364098573 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) - 0.018456028825292 * (math.cos(math.radians(degree0_bullet)) * x0_bullet + 605.47369642885 * (
                (math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet)))))) / (
                      (math.cos(math.radians(degree0_bullet))) ** 2))

        if (t1 > t2):
            return t1, w1
        else:
            return t2, w2

    def min():
        t1 = ((0.45152364098575 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) + 11.174639994247 * ((math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet))))) / (
                      math.cos(math.radians(degree0_bullet)) * (
                      math.cos(math.radians(degree0_bullet)) - 0.41247895569216)))
        w1 = ((0.45152364098573 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) + 0.018456028825292 * (math.cos(math.radians(degree0_bullet)) * x0_bullet + 605.47369642885 * (
                (math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet)))))) / (
                      (math.cos(math.radians(degree0_bullet))) ** (2)))

        t2 = ((-0.45152364098575 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) - 11.174639994247 * ((math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet))))) / (
                      math.cos(math.radians(degree0_bullet)) * (
                      math.cos(math.radians(degree0_bullet)) - 0.41247895569216)))
        w2 = ((-0.45152364098573 * (abs(math.cos(math.radians(degree0_bullet)) - 0.41247895569216) * math.sqrt(
            math.sin(math.radians(degree0_bullet)) * math.cos(
                math.radians(degree0_bullet)) * x0_bullet + 124.87257900102 * (
                    math.cos(math.radians(degree0_bullet)) - math.sin(math.radians(degree0_bullet))) ** (
                2)) - 0.018456028825292 * (math.cos(math.radians(degree0_bullet)) * x0_bullet + 605.47369642885 * (
                (math.cos(math.radians(degree0_bullet))) ** (2) - (
                math.sin(math.radians(degree0_bullet)) + 0.41247895569216) * math.cos(
            math.radians(degree0_bullet)) + 0.41247895569215 * math.sin(math.radians(degree0_bullet)))))) / (
                      (math.cos(math.radians(degree0_bullet))) ** 2))

