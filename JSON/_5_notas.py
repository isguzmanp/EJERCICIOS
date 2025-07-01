import json

with open('JSON/notas.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

estudiante = input("Ingrese el código del estudiante: ")
notas = datos.get(estudiante)

if notas:
    promedio = sum(notas) / len(notas)
    with open(f'JSON/NUEVOS_JSON/promedio_estudiante_{estudiante}.json', 'w', encoding='utf-8') as salida:
        json.dump({estudiante: promedio}, salida, indent=4)
    print("Archivo generado con éxito.")
else:
    print("Estudiante no encontrado.")
