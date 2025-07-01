import json

with open('JSON/usuarios.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

edad_min = int(input("Edad mínima: "))
edad_max = int(input("Edad máxima: "))

print(f"\nPersonas entre {edad_min} y {edad_max} años:")
for info in datos.values():
    if edad_min <= info['edad'] <= edad_max:
        print(f"- {info['nombres']} {info['apellidos']}")