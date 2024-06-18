# Definición de constantes
MAX_ASIENTOS = 100
PRECIOS = {
    'Platinum': 120000,
    'Gold': 80000,
    'Silver': 50000
}

# Listas para almacenar información
asientos_disponibles = ['O'] * MAX_ASIENTOS  # 'O' indica disponible, 'X' indica vendido
asistentes = []

# Función para comprar entradas
def comprar_entradas():
    cantidad = 0  # Inicializamos cantidad fuera del try-except
    
    try:
        cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return
    
    while cantidad < 1 or cantidad > 3:
        try:
            cantidad = int(input("Cantidad inválida. Ingrese nuevamente (entre 1 y 3): "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            continue

    print("Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()

    entradas_compradas = []
    for i in range(cantidad):
        ubicacion = 0  # Inicializamos ubicacion dentro del for
        try:
            ubicacion = int(input(f"Ingrese el número de asiento para la entrada {i + 1}: "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            continue
        
        while ubicacion < 1 or ubicacion > MAX_ASIENTOS or asientos_disponibles[ubicacion - 1] == 'X':
            print("Ubicación no disponible. Intente con otra.")
            try:
                ubicacion = int(input(f"Ingrese el número de asiento para la entrada {i + 1}: "))
            except ValueError:
                print("Error: Debe ingresar un número entero.")
                continue

        asientos_disponibles[ubicacion - 1] = 'X'
        entradas_compradas.append(ubicacion)

    run = input("Ingrese el RUN (sin puntos ni guión): ")
    while not run.isdigit():
        run = input("RUN inválido. Ingrese nuevamente (solo números): ")

    asistentes.append((run, entradas_compradas))
    print("Operación realizada correctamente.")


def mostrar_ubicaciones_disponibles():
    print("Estado actual de la venta de entradas:")
    
    # Función auxiliar para imprimir en columnas de 10 elementos
    def imprimir_en_columnas(asientos):
        for i in range(0, len(asientos), 10):
            print(" ".join(asientos[i:i+10]))
    
    # Mostramos el estado de cada categoría de asientos
    print("Platinum (Asientos del 1 al 20):")
    imprimir_en_columnas(asientos_disponibles[0:20])
    
    print("Gold (Asientos del 21 al 50):")
    imprimir_en_columnas(asientos_disponibles[20:50])
    
    print("Silver (Asientos del 51 al 100):")
    imprimir_en_columnas(asientos_disponibles[50:100])



# Función para ver listado de asistentes
def ver_listado_asistentes():
    if not asistentes:
        print("Aún no hay asistentes registrados.")
    else:
        print("Listado de asistentes por RUN:")
        for run, entradas in sorted(asistentes):
            print(f"{run}: {', '.join(map(str, entradas))}")

def mostrar_ganancias_totales():
    total = 0
    total_cantidad = 0  # Variable para sumar la cantidad total de asientos vendidos

    for tipo, precio in PRECIOS.items():
        cantidad = sum(asientos_disponibles[i] == 'X' for i in range(len(asientos_disponibles)) if (tipo == 'Platinum' and 0 <= i < 20) or (tipo == 'Gold' and 20 <= i < 50) or (tipo == 'Silver' and 50 <= i < 100))
        ganancia = cantidad * precio
        total += ganancia
        total_cantidad += cantidad  # Sumamos la cantidad de asientos vendidos
        
        print(f"{tipo:10} ${precio:>9,} {cantidad:>5} {ganancia:>10,}")

    print(f"TOTAL      {total_cantidad:>20} {total:>10,}")


# Función principal del programa
def main():
    while True:
        print("\n--- Menú ---")
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de asistentes")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            comprar_entradas()
        elif opcion == '2':
            mostrar_ubicaciones_disponibles()
        elif opcion == '3':
            ver_listado_asistentes()
        elif opcion == '4':
            mostrar_ganancias_totales()
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
