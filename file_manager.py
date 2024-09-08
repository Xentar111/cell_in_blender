import os
from keras.models import load_model
from cell_object import Cell

def save_genes(cells, filename='genes'):
    os.makedirs('models', exist_ok=True)
    for i, cell in enumerate(cells):
        cell.brain.save(os.path.join('models', f'{filename}_cell_{i}.h5'))
    print(f'Modelos guardados en el directorio "models/" con prefijo "{filename}_cell_"')

def load_genes(directory='models', prefix='genes'):
    loaded_cells = []
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith('.h5'):
            model = load_model(os.path.join(directory, filename))
            cell = Cell()
            cell.brain = model
            loaded_cells.append(cell)
    print(f'Cargados {len(loaded_cells)} modelos desde el directorio "{directory}"')
    return loaded_cells