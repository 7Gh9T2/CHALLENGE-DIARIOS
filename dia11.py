

#Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine si un número está en una lista 
#ordenada de 10 elementos.

def busqueda_binaria(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return True
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False


lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numero = 10

if busqueda_binaria(lista, numero):
    print(f"El número {numero} está en la lista.")
else:
    print(f"El número {numero} no está en la lista.")

