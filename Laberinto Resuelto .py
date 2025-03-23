import matplotlib.pyplot as plt
import numpy as np
import time

laberinto = [
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
]

"""# Definimos el laberinto con solucion
laberinto = [
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
]"""


def resolver_laberinto(laberinto, x, y, visitado, camino, axs, delay=0.3):
    # Verificamos que la posición sea válida
    if 0 <= x < 10 and 0 <= y < 10 and laberinto[x][y] == 0 and not visitado[x][y]:
        # Marcamos como visitado
        visitado[x][y] = True
        camino.append((x, y))

        # Actualizamos la visualización
        actualizar_visualizacion(axs, camino, "Resolviendo el laberinto...")
        time.sleep(delay) 

        # encontramos la solución
        if x == 9 and y == 9:
            actualizar_visualizacion(axs, camino, "¡Laberinto resuelto! Llegaste a la meta.")
            return True

        
        if resolver_laberinto(laberinto, x + 1, y, visitado, camino, axs, delay):  # Abajo
            return True
        if resolver_laberinto(laberinto, x, y + 1, visitado, camino, axs, delay):  # Derecha
            return True
        if resolver_laberinto(laberinto, x, y - 1, visitado, camino, axs, delay):  # Izquierda
            return True
        if resolver_laberinto(laberinto, x - 1, y, visitado, camino, axs, delay):  # Arriba
            return True

        camino.pop()  # Retrocede si no es el camino correcto
        visitado[x][y] = False

    return False

# Función principal
def resolver(laberinto, axs, delay=0.3):
    visitado = [[False for _ in range(10)] for _ in range(10)]
    camino = []
    encontrado = resolver_laberinto(laberinto, 0, 0, visitado, camino, axs, delay)

    # Si no se encontró solución, igual se muestra el avance
    if not encontrado:
        actualizar_visualizacion(axs, camino, "Laberinto sin solución")

# Función para actualizar la visualización
def actualizar_visualizacion(axs, camino, mensaje):
    laberinto_array = np.array(laberinto)
    axs.clear()
    axs.imshow(laberinto_array, cmap="binary")
    axs.set_title(mensaje)

    if camino:
        x, y = zip(*camino)
        axs.plot(y, x, color="red", linewidth=2)

    axs.grid(True, color="gray")
    axs.set_xticks(np.arange(-0.5, 10, 1), [])
    axs.set_yticks(np.arange(-0.5, 10, 1), [])
    axs.set_xticks(np.arange(0.5, 10, 1), minor=True)
    axs.set_yticks(np.arange(0.5, 10, 1), minor=True)
    axs.grid(which='minor', color='gray', linestyle='-', linewidth=1)
    plt.draw()
    plt.pause(0.01)

# Visualización dinámica
def visualizar_laberinto_dinamico(laberinto, delay=0.3):
    fig, axs = plt.subplots(figsize=(6, 6))
    plt.ion()  # Modo interactivo encendido
    resolver(laberinto, axs, delay)
    plt.ioff()  # Modo interactivo apagado
    plt.show()

# Ejecuta visualización paso a paso
visualizar_laberinto_dinamico(laberinto)
