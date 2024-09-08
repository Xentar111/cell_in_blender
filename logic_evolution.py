import numpy as np

from cell_object import Cell
from environment import draw_environment, food_positions
from gen_cell import save_genes

cells = [Cell() for _ in range(10)]

for _ in range(100):  # 100 ciclos de vida
    for cell in cells:
        if cell.energy > 0:
            cell.move()
            nearest_food = cell.find_food(food_positions)
            # Si la célula llega a la posición de la comida, gana energía
            if np.array_equal([cell.x, cell.y], nearest_food):
                cell.energy += 20
                food_positions = np.delete(food_positions, np.where(food_positions == nearest_food), axis=0)
    
    draw_environment(cells, food_positions)
    
    # Reproducción: las células con más energía sobreviven y se reproducen
    cells = sorted(cells, key=lambda c: c.energy, reverse=True)[:5]  # Mantener las 5 más fuertes
    cells.extend([Cell() for _ in range(5)])  # Añadir nuevas células para mantener el total


if __name__ == '__main__':
    # Ejemplo de uso
    save_genes(cells, generation=1)