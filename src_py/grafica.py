import matplotlib.pyplot as plt

def Grafica():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Crear in grafico en líneas
    plt.plot (x, y, label = "linea", color = "blue")

    # Agregar parámetros
    plt.title ("Mi primer gráfico")
    plt.xlabel ("eje de la x")
    plt.ylabel ("eje de la y")

    plt.legend()


