import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Définir les fonctions représentant les deux courbes
def curve1(x):
    return np.sin(x)

def curve2(x):
    return np.cos(x)

# Définir la fonction d'équation pour fsolve
def intersection_equation(x):
    return curve1(x) - curve2(x)

# Estimation initiale du point d'intersection
initial_guess = [1.0]

# Utiliser fsolve pour trouver le point d'intersection
intersection_point = fsolve(intersection_equation, initial_guess)

# Afficher le point d'intersection
print("Point d'intersection :", intersection_point)

# Tracer les courbes
x_values = np.linspace(0, 2 * np.pi, 100)
plt.plot(x_values, curve1(x_values), label="Courbe 1: sin(x)")
plt.plot(x_values, curve2(x_values), label="Courbe 2: cos(x)")
plt.scatter(intersection_point, curve1(intersection_point), color='red', label="Point d'intersection")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Intersection de deux courbes")
plt.grid(True)
plt.show()
