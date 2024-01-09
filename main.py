import math
import matplotlib.pyplot as plt
import numpy as np
from Disc import Disc
from Bullet import Bullet
from Contact import Contact


# User input parameters for the disk
speed0_disc = 70
degree0_disc = 45

# Calculating paths for the disc
disc = Disc(speed0_disc, degree0_disc)
x_d, y_d = disc.calculate_trajectory()

# User input parameters for rifle bullet
speed0_bullet = 120
degree0_bullet = float(input("Veuillez entrer l'angle de tir de la balle de fusil en degrés : "))

while (degree0_bullet < 0 or degree0_bullet > 180) :
    degree0_bullet = float(input("Veuillez entrer l'angle de tir entre 0 et 180 degré : "))

x0_bullet = float(input("Veuillez entrer la position horizontale initiale de la balle de fusil en m : "))
y0_bullet = 0


# Calculating trajectories for rifle bullets
bullet = Bullet(speed0_bullet, degree0_bullet, x0_bullet)
contact = Contact(bullet)
contact.contact()
bullet.set_wait(contact.get_wait_time())
x_b, y_b = bullet.calculate_trajectory(disc.get_fight_time())

print(contact.get_touch_time())
x_t, y_t = bullet.position_on_time(contact.get_touch_time())

# Results display
print(f"------------ Données du disc ------------")
print(f"Vitesse de départ du disque : {speed0_disc:.2f} m/s")
print(f"Degré de départ du disque : {degree0_disc:.2f}°")
print(f"Portée maximale du disque : {disc.get_horizontal_maximum():.2f} m")
print(f"Temps de vol du disque : {disc.get_fight_time():.2f} s")
print(f"Hauteur maximale du disque : {disc.get_vertical_maximum():.2f} m")

print(f"-----------------------------------------")
print(f"------------ Données du tir ------------")
print(f"Vitesse de départ du tir: {speed0_bullet:.2f} m/s")
print(f"Degré de départ du tir : {degree0_bullet:.2f}°")
print(f"Temp d'attente avant tir : {contact.get_wait_time():.2f} s")

print(f"-----------------------------------------")
print(f"------------ Données de contact ------------")
print(f"Moment de contact : {contact.get_touch_time():.2f} s")
print(f"Position (x,y) du contact : x{x_t:.2f}, y{y_t:.2f}")

# Plotting the trajectory of the disc and the bullet on the same graph

plt.plot(x_d, y_d, label="Trajectoire du disque")
plt.plot(x_b, y_b, label="Trajectoire de la balle de fusil", linestyle='dashed')
plt.scatter(*bullet.position_on_time(contact.get_touch_time()), color='red', label="Point d'intersection")
plt.legend()
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
