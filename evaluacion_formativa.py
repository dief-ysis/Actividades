import os

# Definición de constantes
CARGOS = ['CEO', 'Desarrollador', 'Analista de datos']
DESC_SALUD = 70000
DESC_AFP = 120000

# Lista para almacenar trabajadores
trabajadores = []

# Función para registrar un trabajador
def registrar_trabajador():
    print("\nRegistro de Trabajador")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cargo = input(f"Ingrese el cargo ({', '.join(CARGOS)}): ")
    while cargo not in CARGOS:
        print("Cargo no válido. Los cargos válidos son:", ', '.join(CARGOS))
        cargo = input("Ingrese el cargo: ")
    sueldo_bruto = float(input("Ingrese el sueldo bruto: "))
    
    # Calcular descuentos y líquido a pagar
    desc_salud = DESC_SALUD
    desc_afp = DESC_AFP
    sueldo_liquido = sueldo_bruto - desc_salud - desc_afp
    
    # Agregar trabajador a la lista
    trabajadores.append({
        'Nombre': nombre,
        'Apellido': apellido,
        'Cargo': cargo,
        'Sueldo Bruto': sueldo_bruto,
        'Descuento Salud': desc_salud,
        'Descuento AFP': desc_afp,
        'Líquido a pagar': sueldo_liquido
    })
    
    print("Trabajador registrado correctamente.")

# Función para listar todos los trabajadores
def listar_trabajadores():
    if not trabajadores:
        print("No hay trabajadores registrados.")
    else:
        print("\nListado de Trabajadores:")
        for idx, trabajador in enumerate(trabajadores, start=1):
            print(f"{idx}. {trabajador['Nombre']} {trabajador['Apellido']}, Cargo: {trabajador['Cargo']}, Sueldo Bruto: {trabajador['Sueldo Bruto']}, Desc. Salud: {trabajador['Descuento Salud']}, Desc. AFP: {trabajador['Descuento AFP']}, Líquido a pagar: {trabajador['Líquido a pagar']}")

# Función para imprimir planilla de sueldos
def imprimir_planilla():
    if not trabajadores:
        print("No hay trabajadores registrados para imprimir la planilla.")
        return
    
    print("\nImprimir Planilla de Sueldos:")
    print("1. Imprimir para todos los trabajadores")
    print("2. Imprimir por cargo específico")
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre_archivo = "planilla_sueldos_todos.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("Planilla de Sueldos - Todos los Trabajadores\n")
            archivo.write("=================================================\n")
            for trabajador in trabajadores:
                archivo.write(f"Nombre: {trabajador['Nombre']} {trabajador['Apellido']}\n")
                archivo.write(f"Cargo: {trabajador['Cargo']}\n")
                archivo.write(f"Sueldo Bruto: {trabajador['Sueldo Bruto']}\n")
                archivo.write(f"Descuento Salud: {trabajador['Descuento Salud']}\n")
                archivo.write(f"Descuento AFP: {trabajador['Descuento AFP']}\n")
                archivo.write(f"Líquido a pagar: {trabajador['Líquido a pagar']}\n")
                archivo.write("-------------------------------------------------\n")
        print(f"Se ha generado el archivo '{nombre_archivo}' con éxito.")
    
    elif opcion == '2':
        print("Cargos disponibles:", ', '.join(CARGOS))
        cargo = input("Seleccione un cargo para imprimir: ")
        while cargo not in CARGOS:
            print("Cargo no válido. Los cargos válidos son:", ', '.join(CARGOS))
            cargo = input("Seleccione un cargo para imprimir: ")
        
        nombre_archivo = f"planilla_sueldos_{cargo.lower().replace(' ', '_')}.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(f"Planilla de Sueldos - Cargo: {cargo}\n")
            archivo.write("=================================================\n")
            for trabajador in trabajadores:
                if trabajador['Cargo'] == cargo:
                    archivo.write(f"Nombre: {trabajador['Nombre']} {trabajador['Apellido']}\n")
                    archivo.write(f"Sueldo Bruto: {trabajador['Sueldo Bruto']}\n")
                    archivo.write(f"Descuento Salud: {trabajador['Descuento Salud']}\n")
                    archivo.write(f"Descuento AFP: {trabajador['Descuento AFP']}\n")
                    archivo.write(f"Líquido a pagar: {trabajador['Líquido a pagar']}\n")
                    archivo.write("-------------------------------------------------\n")
        print(f"Se ha generado el archivo '{nombre_archivo}' con éxito.")
    
    else:
        print("Opción no válida.")

# Función principal del programa
def main():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar trabajador")
        print("2. Listar todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del Programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_trabajador()
        elif opcion == '2':
            listar_trabajadores()
        elif opcion == '3':
            imprimir_planilla()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
