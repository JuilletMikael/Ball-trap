import math
import matplotlib.pyplot as plt
import numpy as np
from Disc import Disc
from Bullet import Bullet

# User input parameters for the disk
speed0_disc = 70
degree0_disc = 45

# Calculating paths for the disc
disc = Disc(speed0_disc, degree0_disc)
x_d, y_d, v_d, R_d, t_flight_d, H_d, t_d = disc.calculate_trajectory()

# User input parameters for rifle bullet
speed0_bullet = 120
degree0_bullet = float(input("Veuillez entrer l'angle de tir de la balle de fusil en degrés : "))

while (degree0_bullet < 0 or degree0_bullet > 180) :
    degree0_bullet = float(input("Veuillez entrer l'angle de tir entre 0 et 180 degré : "))

x0_bullet = float(input("Veuillez entrer la position horizontale initiale de la balle de fusil en m : "))
y0_bullet = 0


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




    if (t1 < t2):
        return t1, w1
    else:
        return t2, w2

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


if (degree0_bullet >= 90) :
    # Adding 0.01 on 90 degree to avoid crash
    # TODO : Fix 90 degree
    if (degree0_bullet == 90) :
        degree0_bullet = degree0_bullet + 0.001
    t, w = min()

if (degree0_bullet < 90):
    t, w = max()

# Calculating trajectories for rifle bullets
bullet = Bullet(speed0_bullet, degree0_bullet, x0_bullet, w)
x_b, y_b, t_b = bullet.calculate_trajectory(t_flight_d)
x_t, y_t = bullet.position_on_time(t)

# Results display
print(f"------------ Données du disc ------------")
print(f"Vitesse de départ du disque : {speed0_disc:.2f} m/s")
print(f"Degré de départ du disque : {degree0_disc:.2f}°")
print(f"Portée maximale du disque : {R_d:.2f} m")
print(f"Temps de vol du disque : {t_flight_d:.2f} s")
print(f"Hauteur maximale du disque : {H_d:.2f} m")

print(f"-----------------------------------------")
print(f"------------ Données du tir ------------")
print(f"Vitesse de départ du tir: {speed0_bullet:.2f} m/s")
print(f"Degré de départ du tir : {degree0_bullet:.2f}°")
print(f"Temp d'attente avant tir : {w:.2f} s")

print(f"-----------------------------------------")
print(f"------------ Données de contact ------------")
print(f"Moment de contact : {t:.2f} s")
print(f"Position (x,y) du contact : x{x_t:.2f}, y{y_t:.2f}")

# Plotting the trajectory of the disc and the bullet on the same graph
plt.figure(figsize=(8, 6))
plt.plot(x_d, y_d, label="Trajectoire du disque")
plt.plot(x_b, y_b, label="Trajectoire de la balle de fusil", linestyle='dashed')
plt.title("Trajectoire du disque et de la balle de fusil avec point d'intersection")
plt.xlabel("Distance (m)")
plt.ylabel("Hauteur (m)")
plt.scatter(*bullet.position_on_time(t), color='red', label="Point d'intersection")
plt.legend()
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
