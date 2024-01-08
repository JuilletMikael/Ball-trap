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
