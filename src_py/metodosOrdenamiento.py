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
    
    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
                for i in range(gap, n):
                        temp = arreglo[i]
                        j = i
                        while j >= gap and arreglo[j - gap] > temp:
                                arreglo[j] = arreglo[j - gap]
                                j -= gap
                        arreglo[j] = temp
                gap //= 2

        return arreglo