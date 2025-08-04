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

def agregar_estudiante():
    try:
        id_estudiante = input("Ingrese el ID del estudiante: ").strip()
        if id_estudiante in estudiantes:
            print("Este ID ya está registrado.")
            return
        nombre = input("Ingrese el nombre completo: ").strip()
        carrera = input("Ingrese la carrera o programa académico: ").strip()

        estudiantes[id_estudiante] = {
            "nombre": nombre,
            "carrera": carrera,
            "cursos": {}
        }
        print("Estudiante registrado exitosamente.")
    except Exception as e:
        print("Error al agregar estudiante:", e)

def agregar_curso():
    try:
        id_estudiante = input("Ingrese el ID del estudiante: ").strip()
        if id_estudiante not in estudiantes:
            print("Estudiante no encontrado.")
            return

        curso = input("Ingrese el nombre del curso: ").strip()
        nota = float(input("Ingrese la nota final (0-100): "))
        if nota < 0 or nota > 100:
            print("Nota fuera de rango.")
            return

        estudiantes[id_estudiante]["cursos"][curso] = nota
        print("Curso agregado correctamente.")
    except ValueError:
        print("La nota debe ser un número.")
    except Exception as e:
        print("Error al agregar curso:", e)

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