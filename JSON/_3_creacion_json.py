import json

with open('JSON/usuarios.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

deportes_dict = {}
for usuario, info in datos.items():
    for deporte in info['deportes']:
        deportes_dict.setdefault(deporte, []).append(usuario)

with open('JSON/NUEVOS_JSON/usuario_deportes.json', 'w', encoding='utf-8') as salida:
    json.dump(deportes_dict, salida, indent=4, ensure_ascii=False)

print("Archivo 'usuario_deportes.json' generado con éxito.")
