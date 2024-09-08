import numpy as np
from cell_object import Cell
from file_manager import save_genes, load_genes
from visualizer import draw_environment

# Crear posiciones aleatorias para la comida
env_size = 100
num_food_items = 20
food_positions = np.random.randint(0, env_size, size=(num_food_items, 2))

# Cargar células de modelos previos si existen, o crear nuevas
cells = load_genes(directory='models', prefix='genes_gen_99')  # Carga la última generación guardada

if len(cells) == 0:  # Si no se encuentran modelos previos
    initial_population_size = 10
    cells = [Cell() for _ in range(initial_population_size)]

# Repetir el ciclo de vida de las células
for generation in range(100, 200):
    for cell in cells:
        if cell.energy > 0:
            cell.move()
            nearest_food = cell.find_food(food_positions)
            
            # Verificar si la célula ha encontrado comida
            if any(np.array_equal([cell.x, cell.y], food) for food in food_positions):
                cell.energy += 20
                # Eliminar la comida consumida de las posiciones de comida
                food_positions = np.array([food for food in food_positions if not np.array_equal([cell.x, cell.y], food)])
    
    # Dibujar el estado actual del entorno
    draw_environment(cells, food_positions)
    
    # Reproducción: las células con más energía sobreviven y se reproducen
    cells = sorted(cells, key=lambda c: c.energy, reverse=True)[:5]
    cells.extend([Cell() for _ in range(5)])

    # Guardar modelos al final de cada generación
    save_genes(cells, filename=f'genes_gen_{generation}')