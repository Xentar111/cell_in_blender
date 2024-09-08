import matplotlib.pyplot as plt


env_size = 100
def draw_environment(cells, food_positions):
    plt.clf()  # Limpiar la figura para evitar sobreposición de frames
    
    # Dibujar células
    for cell in cells:
        plt.plot(cell.x, cell.y, 'ro')  # 'ro' significa puntos rojos para las células
    
    # Dibujar comida
    for food in food_positions:
        plt.plot(food[0], food[1], 'go')  # 'go' significa puntos verdes para la comida
    
    # Configuración del entorno de visualización
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)  # Mostrar una cuadrícula para una mejor referencia visual
    plt.draw()
    plt.pause(0.1)  # Pausa de 0.1 segundos entre cuadros para una animación más clara