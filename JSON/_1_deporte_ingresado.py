import json

with open('JSON/usuarios.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

deporte_buscado = input("Ingrese un deporte: ").strip().lower()

print("\nPersonas que practican", deporte_buscado.title())
for usuario, info in datos.items():
    if deporte_buscado in [d.lower() for d in info['deportes']]:
        print(f"- {info['nombres']} {info['apellidos']}")
