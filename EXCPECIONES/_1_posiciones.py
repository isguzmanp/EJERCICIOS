lista = [1, 2, 3, 4]

try:
    print(lista[5])
except IndexError:
    print("Intenta acceder una posición que no está en el arreglo")
