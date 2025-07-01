def operar(a, b):
    return a + b

def main():
    try:
        a = int(input("Ingrese un número: "))
        b = 'hola'
        operar(a, b)
    except TypeError:
        print("Los tipos de datos no cuadran para hacer la operación")

main()


