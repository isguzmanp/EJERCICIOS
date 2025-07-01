import csv

medio_dado = input("Ingresa el medio de pago: ").strip().lower()

contador = 0

with open('ARCHIVOS/SalesJan2009.csv', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        if fila['Payment_Type'].strip().lower() == medio_dado:
            contador += 1

print(f"Número de compras realizadas con {medio_dado.title()}: {contador}")