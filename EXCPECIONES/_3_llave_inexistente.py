def main():
    try:
        dict = {'James': 'Java', 'Dennis': 'C', 'Das': 'Python'}
        print(dict['Ada'])
    except KeyError:
        print("Intenta acceder una llave que no está en el diccionario")

main()
