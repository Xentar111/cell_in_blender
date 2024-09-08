

# Guardar las características de las células sobrevivientes
def save_genes(cells, generation):
    with open(f'genes_gen_{generation}.txt', 'w') as file:
        for cell in cells:
            file.write(f'{cell.x},{cell.y},{cell.energy}\n')


