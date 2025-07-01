import json

with open('JSON/coincidencia_1.json', encoding='utf-8') as f1, open('JSON/coincidencia_2.json', encoding='utf-8') as f2:
    json1 = json.load(f1)
    json2 = json.load(f2)

coincidencias = {k: v for k, v in json1.items() if k in json2 and json2[k] == v}

with open('JSON/NUEVOS_JSON/coincidencias.json', 'w', encoding='utf-8') as salida:
    json.dump(coincidencias, salida, indent=4, ensure_ascii=False)
