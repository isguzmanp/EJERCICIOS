import csv

pais_dado = input("Ingresa el país: ").strip().lower()

contador = 0

with open('ARCHIVOS/SalesJan2009.csv', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        if fila['Country'].strip().lower() == pais_dado:
            contador += 1

print(f"Número de compras en {pais_dado.title()}: {contador}")

