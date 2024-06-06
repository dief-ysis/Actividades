import csv
import json

def clasificar_empresa(ventas):
    if ventas > 200000000:
        return "Gran Contribuyente"
    elif 100000001 <= ventas <= 200000000:
        return "Mediano Contribuyente"
    else:
        return "Pequeño Contribuyente"

with open('listadoRutEmpresa.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    data = [] 

    for fila in lector_csv:
        rut = fila["rut"]
        nombre = fila["nombre"]
        ventas = int(fila["ventas"])
        clasificacionEmpresa = clasificar_empresa(ventas)

        print(f"La empresa {nombre}, Rut:{rut}, es {clasificacionEmpresa} y tiene una contribucion de {ventas}")

        fila["Clasificacion Empresa"] = clasificacionEmpresa
        data.append(fila)

with open('segmentacionEmpresas.json', 'w') as archivo:
    json.dump(data, archivo, indent=4)