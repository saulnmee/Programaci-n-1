while True:
    LISTA = int(input("""
    1. MATEMATICAS
    2. ESPAÑOL
    3. CIENCIAS
    4. HISTORIA
    5. PROGRAMACION
    Elige una materia: 
    """))

    match LISTA:

        case 1:
            alumnos = ["ana", "sofia", "elioth", "santiago", "karla", "marisol"]
            aula = "22"
            maestro = "maestro juan padilla"

            print("Hola, están en el curso de Matemáticas. ¡Bienvenidos!")
            print("El total de personas aquí es:", len(alumnos))
            print("Los alumnos son:", alumnos)
            print("El aula es:", aula)
            print("El maestro actual es:", maestro)

            expu = input("¿Alta o baja a un alumno? ").lower()

            if expu == "alta":
                agregar = input("Nombre del alumno que quieres agregar: ")
                alumnos.append(agregar)
                print("Alumno agregado correctamente.")
            elif expu == "baja":
                sacar = input("Nombre del alumno que quieres eliminar: ")
                if sacar in alumnos:
                    alumnos.remove(sacar)
                    print("Alumno eliminado correctamente.")
                else:
                    print("Ese alumno no está en la lista.")

            # 👉 Mostrar lista actualizada
            print("La nueva lista de alumnos es:", alumnos)

            pregunta1 = input("¿Quieres cambiar el número del aula? ").lower()
            if pregunta1 == "si":
                aula2 = input("¿Cuál será la nueva aula? ")
                aula = aula2
                print("La nueva aula será:", aula)

            otro = input("¿Cambiará el maestro? ").lower()
            if otro == "si":
                nuevo = input("¿Quién será el nuevo profe? ")
                maestro = nuevo
                print("El nuevo maestro es:", maestro)

            final = input("¿Quieres terminar? ").lower()
            if final == "si":
                break

        case 2:
            alumnos = ["jose", "maria", "cesar", "adriana", "karla", "susana"]
            aula = "11"
            maestro = "maestro moran gilberto"

            print("Hola, están en el curso de Español. ¡Bienvenidos!")
            print("El total de personas aquí es:", len(alumnos))
            print("Los alumnos son:", alumnos)
            print("El aula es:", aula)
            print("El maestro actual es:", maestro)

            expu = input("¿Alta o baja a un alumno? ").lower()

            if expu == "alta":
                agregar = input("Nombre del alumno que quieres agregar: ")
                alumnos.append(agregar)
                print("Alumno agregado correctamente.")
            elif expu == "baja":
                sacar = input("Nombre del alumno que quieres eliminar: ")
                if sacar in alumnos:
                    alumnos.remove(sacar)
                    print("Alumno eliminado correctamente.")
                else:
                    print("Ese alumno no está en la lista.")

            print("La nueva lista de alumnos es:", alumnos)

            pregunta1 = input("¿Quieres cambiar el número del aula? ").lower()
            if pregunta1 == "si":
                aula2 = input("¿Cuál será la nueva aula? ")
                aula = aula2
                print("La nueva aula será:", aula)

            otro = input("¿Cambiará el maestro? ").lower()
            if otro == "si":
                nuevo = input("¿Quién será el nuevo profe? ")
                maestro = nuevo
                print("El nuevo maestro es:", maestro)

            final = input("¿Quieres terminar? ").lower()
            if final == "si":
                break

        case 3:
            alumnos = ["miguel", "sofia", "pedro", "isabel", "diego", "valeria"]
            aula = "8"
            maestro = "maestro roberto salas"

            print("Hola, están en el curso de Ciencias. ¡Bienvenidos!")
            print("El total de personas aquí es:", len(alumnos))
            print("Los alumnos son:", alumnos)
            print("El aula es:", aula)
            print("El maestro actual es:", maestro)

            expu = input("¿Alta o baja a un alumno? ").lower()

            if expu == "alta":
                agregar = input("Nombre del alumno que quieres agregar: ")
                alumnos.append(agregar)
                print("Alumno agregado correctamente.")
            elif expu == "baja":
                sacar = input("Nombre del alumno que quieres eliminar: ")
                if sacar in alumnos:
                    alumnos.remove(sacar)
                    print("Alumno eliminado correctamente.")
                else:
                    print("Ese alumno no está en la lista.")

            print("La nueva lista de alumnos es:", alumnos)

            pregunta1 = input("¿Quieres cambiar el número del aula? ").lower()
            if pregunta1 == "si":
                aula2 = input("¿Cuál será la nueva aula? ")
                aula = aula2
                print("La nueva aula será:", aula)

            otro = input("¿Cambiará el maestro? ").lower()
            if otro == "si":
                nuevo = input("¿Quién será el nuevo profe? ")
                maestro = nuevo
                print("El nuevo maestro es:", maestro)

            final = input("¿Quieres terminar? ").lower()
            if final == "si":
                break

        case 4:
            alumnos = ["fernanda", "carlos", "marco", "diana", "julio", "rocio"]
            aula = "5"
            maestro = "maestra luisa garcía"

            print("Hola, están en el curso de Historia. ¡Bienvenidos!")
            print("El total de personas aquí es:", len(alumnos))
            print("Los alumnos son:", alumnos)
            print("El aula es:", aula)
            print("El maestro actual es:", maestro)

            expu = input("¿Alta o baja a un alumno? ").lower()

            if expu == "alta":
                agregar = input("Nombre del alumno que quieres agregar: ")
                alumnos.append(agregar)
                print("Alumno agregado correctamente.")
            elif expu == "baja":
                sacar = input("Nombre del alumno que quieres eliminar: ")
                if sacar in alumnos:
                    alumnos.remove(sacar)
                    print("Alumno eliminado correctamente.")
                else:
                    print("Ese alumno no está en la lista.")

            print("La nueva lista de alumnos es:", alumnos)

            pregunta1 = input("¿Quieres cambiar el número del aula? ").lower()
            if pregunta1 == "si":
                aula2 = input("¿Cuál será la nueva aula? ")
                aula = aula2
                print("La nueva aula será:", aula)

            otro = input("¿Cambiará el maestro? ").lower()
            if otro == "si":
                nuevo = input("¿Quién será el nuevo profe? ")
                maestro = nuevo
                print("El nuevo maestro es:", maestro)

            final = input("¿Quieres terminar? ").lower()
            if final == "si":
                break

        case 5:
            alumnos = ["alejandro", "luis", "sofia", "mario", "andrea", "paola"]
            aula = "19"
            maestro = "maestro carlos ramírez"

            print("Hola, están en el curso de Programación. ¡Bienvenidos!")
            print("El total de personas aquí es:", len(alumnos))
            print("Los alumnos son:", alumnos)
            print("El aula es:", aula)
            print("El maestro actual es:", maestro)

            expu = input("¿Alta o baja a un alumno? ").lower()

            if expu == "alta":
                agregar = input("Nombre del alumno que quieres agregar: ")
                alumnos.append(agregar)
                print("Alumno agregado correctamente.")
            elif expu == "baja":
                sacar = input("Nombre del alumno que quieres eliminar: ")
                if sacar in alumnos:
                    alumnos.remove(sacar)
                    print("Alumno eliminado correctamente.")
                else:
                    print("Ese alumno no está en la lista.")

            print("La nueva lista de alumnos es:", alumnos)

            pregunta1 = input("¿Quieres cambiar el número del aula? ").lower()
            if pregunta1 == "si":
                aula2 = input("¿Cuál será la nueva aula? ")
                aula = aula2
                print("La nueva aula será:", aula)

            otro = input("¿Cambiará el maestro? ").lower()
            if otro == "si":
                nuevo = input("¿Quién será el nuevo profe? ")
                maestro = nuevo
                print("El nuevo maestro es:", maestro)

            final = input("¿Quieres terminar? ").lower()
            if final == "si":
                break

        case _:
            print("Opción no válida. Elige un número del 1 al 5.")
