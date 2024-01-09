import matplotlib.pyplot as plt

class Render(object):

    def figure(self):
        plt.figure(figsize=(8, 6))
        plt.title("Trajectoire du disque et de la balle de fusil avec point d'intersection")
        plt.xlabel("Distance (m)")
        plt.ylabel("Hauteur (m)")

    def bullet(self, bullet):
        plt.plot(bullet.calculate_trajectory(), label="Trajectoire de la balle de fusil", linestyle='dashed')

    def disc(self, disk):
        plt.plot(x_d, y_d, label="Trajectoire du disque")

    def scatter(self, position):
        plt.scatter(*bullet.position_on_time(t), color='red', label="Point d'intersection")

    def final(self):
        plt.legend()
        plt.grid(True)
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.show()

    def consoleInfo(self):
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
