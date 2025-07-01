import json

sustituciones = {
    "$": "a",
    "#": "e",
    "*": "i",
    "¬": "o",
    "+": "u"
}

def desencriptar(cadena):
    for simbolo, vocal in sustituciones.items():
        cadena = cadena.replace(simbolo, vocal)
    return cadena

with open('JSON/encriptados.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

resultado = {clave: desencriptar(valor) for clave, valor in datos.items()}

with open('JSON/NUEVOS_JSON/desencriptados.json', 'w', encoding='utf-8') as salida:
    json.dump(resultado, salida, indent=4, ensure_ascii=False)

print("Archivo desencriptado con éxito.")
