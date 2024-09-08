import os

def save_genes(cells, filename='genes'):
    # Crear un directorio para almacenar los modelos si no existe
    os.makedirs('models', exist_ok=True)
    
    for i, cell in enumerate(cells):
        # Guardar el modelo de cada célula
        cell.brain.save(os.path.join('models', f'{filename}_cell_{i}.h5'))
    print(f'Modelos guardados en el directorio "models/" con prefijo "{filename}_cell_"')
