import benchmarking as bm
from metodosOrdenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()

    # tam = 10000 
    tamanios = [5000, 10000, 15000]
    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        key = "burbuja",
        value = metodosO.sort_bubble

        metodos_dic = {
                "burbuja": metodosO.sort_bubble,
                "seleción": metodosO.sort_selection,
                "inserción": metodosO.sort_insertion,
                "shell": metodosO.sort_shell
        }

        resultados = []

        for nombre, fun_metodo in metodos_dic.items():
                tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
                tupla_resultado = (tam, nombre, tiempo_resultado)
                resultados.append(tupla_resultado)

        for tam, nombre, tiempo in resultados:
            print(f"Tamaño: {tam}, nombre método: {nombre}, tiempo: {tiempo:.6f}")