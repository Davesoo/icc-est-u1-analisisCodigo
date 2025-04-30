class MetodosOrdenamiento:
    
    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
    
    def sort_selection (self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range (n - 1):
            indiceMinimo = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[indiceMinimo]:
                    indiceMinimo = j
            smallerNumber = arreglo[indiceMinimo]
            arreglo[indiceMinimo] = arreglo[i]
            arreglo[i] = smallerNumber
        return arreglo
    
    def sort_insertion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range (n):
            key = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > key:
                arreglo[j + 1]= arreglo[j]
                j = j - 1
            arreglo[j] = key
        return arreglo