estudiantes = {}

def mostrar_menu():
    print("\n--- Sistema de Gestión Académica ---")
    print("1. Agregar estudiante")
    print("2. Agregar curso con nota")
    print("3. Consultar estudiante")
    print("4. Calcular promedio de estudiante")
    print("5. Verificar si aprueba")
    print("6. Mostrar todos los estudiantes")
    print("7. Salir")

def salir_del_programa():
    print("Saliendo del programa...")

    def main():
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    agregar_estudiante()
                case "2":
                    agregar_curso()
                case "3":
                    consultar_estudiante()
                case "4":
                    calcular_promedio()
                case "5":
                    verificar_aprobacion()
                case "6":
                    mostrar_todos()
                case "7":
                    salir_del_programa()
                    break
                case _:
                    print("Opción inválida, intente de nuevo.")

    main()