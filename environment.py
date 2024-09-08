import numpy as np
import matplotlib.pyplot as plt

# Definir el tamaño del entorno
env_size = 100

# Crear posiciones aleatorias para la comida
num_food_items = 20  # Número de elementos de comida
food_positions = np.random.randint(0, env_size, size=(num_food_items, 2))
def draw_environment(cells, food_positions):
    plt.figure(figsize=(6, 6))
    plt.scatter(food_positions[:, 0], food_positions[:, 1], c='green', marker='x', label='Food')
    for cell in cells:
        plt.plot(cell['x'], cell['y'], 'ro', markersize=6)
    plt.xlim(0, env_size)
    plt.ylim(0, env_size)
    plt.legend()
    plt.show()
