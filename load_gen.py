import os

from keras.models import load_model
from cell_object import Cell

def load_genes(directory='output', prefix='genes'):
    loaded_cells = []
    os.makedirs(directory, exist_ok=True)
    
    # Obtener todos los archivos .h5 del directorio especificado
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith('.h5'):
            # Cargar el modelo desde el archivo .h5
            model = load_model(os.path.join(directory, filename))
            
            # Crear una nueva célula con el modelo cargado
            cell = Cell()
            cell.brain = model  # Asignar el modelo cargado a la célula
            loaded_cells.append(cell)
    
    print(f'Cargados {len(loaded_cells)} modelos desde el directorio "{directory}"')
    return loaded_cells
