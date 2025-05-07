import matplotlib.pyplot as plt
import benchmarking as bm
from metodosOrdenamiento import MetodosOrdenamiento
from grafica import Grafica

if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()
    grf = Grafica()

    tamanios = [500, 1000, 2000]
    metodos_dic = {
        "burbuja": metodosO.sort_bubble,
        "selección": metodosO.sort_selection,
        "inserción": metodosO.sort_insertion,
        "shell": metodosO.sort_shell
    }

    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, nombre método: {nombre}, tiempo: {tiempo:.6f}")

    tiempos_by_metodo = {
        "burbuja": [],
        "selección": [],
        "inserción": [],
        "shell": []
    }

    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    for nombre, tiempos in tiempos_by_metodo.items():
        ax1.plot(tamanios, tiempos, label=nombre, marker="o")
    ax1.set_title("Tiempos de ejecución por método")
    ax1.set_xlabel("Tamaño de los arreglos")
    ax1.set_ylabel("Tiempo (s)")
    ax1.legend()
    ax1.grid(True)

    for nombre, tiempos in tiempos_by_metodo.items():
        tiempos_cuadrados = [t**2 for t in tiempos]
        ax2.plot(tamanios, tiempos_cuadrados, label=nombre, marker="s")
    ax2.set_title("Tiempos al cuadrado (ejemplo)")
    ax2.set_xlabel("Tamaño de los arreglos")
    ax2.set_ylabel("Tiempo² (s²)")
    ax2.legend()
    ax2.grid(True)

    plt.suptitle("DAVE SIGÜENZA - 06/05/2025 20:05:25")
    plt.tight_layout()
    plt.show()

