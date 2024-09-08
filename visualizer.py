# visualizer.py

import matplotlib.pyplot as plt

def draw_environment(cells, food_positions):
    plt.clf()
    for cell in cells:
        plt.plot(cell.x, cell.y, 'ro')
    for food in food_positions:
        plt.plot(food[0], food[1], 'go')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.pause(0.01)
