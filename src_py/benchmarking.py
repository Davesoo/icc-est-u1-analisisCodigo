import random
import time
from metodosOrdenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print("Becnmarking instanciado")
        self.mO = MetodosOrdenamiento()
        arreglo = self.build_arreglo(50000)

        tarea = lambda: self.mO.sort_bubble(arreglo)
        tiempo_mili_segundos = self.contar_con_current_time_milles(tarea)
        tiempo_nano_segundos = self.contar_con_nano_time(tarea)
        print("|--------------------------------------------- Método Burbúja ---------------------------------------------|")
        print("Tiempo en milisegundos",tiempo_mili_segundos*1000,f"convertido en segundos: {tiempo_mili_segundos}")
        print("Tiempo en nanosegundos",tiempo_nano_segundos*1000000000,f"convertido en segundos: {tiempo_nano_segundos}")
        
        tarea2 = lambda: self.mO.sort_selection(arreglo)
        tiempo_mili_segundos = self.contar_con_current_time_milles(tarea2)
        tiempo_nano_segundos = self.contar_con_nano_time(tarea2)
        print("|-------------------------------------------- Método Selección --------------------------------------------|")
        print("Tiempo en milisegundos",tiempo_mili_segundos*1000,f"convertido en segundos: {tiempo_mili_segundos}")
        print("Tiempo en nanosegundos",tiempo_nano_segundos*1000000000,f"convertido en segundos: {tiempo_nano_segundos}")

        tarea3 = lambda: self.mO.sort_insertion(arreglo)
        tiempo_mili_segundos = self.contar_con_current_time_milles(tarea3)
        tiempo_nano_segundos = self.contar_con_nano_time(tarea3)
        print("|-------------------------------------------- Método Inserción --------------------------------------------|")
        print("Tiempo en milisegundos",tiempo_mili_segundos*1000,f"convertido en segundos: {tiempo_mili_segundos}")
        print("Tiempo en nanosegundos",tiempo_nano_segundos*1000000000,f"convertido en segundos: {tiempo_nano_segundos}")
        
    def build_arreglo(self, tamaño):
        arreglo = []
        for i in range(tamaño):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0