import numpy as np

from cell_object import Cell
from environment import draw_environment, food_positions
from gen_cell import save_genes
from load_gen import load_genes

# Crear una población inicial de células con posiciones aleatorias
initial_population_size = 10  # Número de células
# Cargar células de modelos previos si existen, o crear nuevas
cells = load_genes(directory='models', prefix='genes_gen_99')  # Carga la última generación guardada

if len(cells) == 0:  # Si no se encuentran modelos previos
    initial_population_size = 10
    cells = [Cell() for _ in range(initial_population_size)]


# Repetir el ciclo de vida de las células
for generation in range(100):  # Por ejemplo, 100 generaciones
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

    # Guardar los modelos al final de cada generación
    save_genes(cells, filename=f'genes_gen_{generation}')

if __name__ == '__main__':
    # Ejemplo de uso
    #save_genes(cells, generation=1)
    pass