import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from visualizer import env_size

class Cell:
    def __init__(self):
        self.x = np.random.randint(0, 100)
        self.y = np.random.randint(0, 100)
        self.energy = 100
        self.brain = self.create_brain()

    def create_brain(self):
        model = Sequential([
            Dense(10, input_dim=2, activation='relu'),
            Dense(5, activation='relu'),
            Dense(2, activation='linear')
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def move(self):
        direction = np.random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.y = min(env_size - 1, self.y + 1)
        elif direction == 'down':
            self.y = max(0, self.y - 1)
        elif direction == 'left':
            self.x = max(0, self.x - 1)
        elif direction == 'right':
            self.x = min(env_size - 1, self.x + 1)

        # Consume energía al moverse
        self.energy -= 1

    def find_food(self, food_positions):
        # Algoritmo de búsqueda para encontrar la comida más cercana
        distances = np.sqrt((food_positions[:, 0] - self.x) ** 2 + (food_positions[:, 1] - self.y) ** 2)
        nearest_food_index = np.argmin(distances)
        return food_positions[nearest_food_index]
