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
            alumnos = ["millan", "saul", "marlon", "carlos", "emiliano", "alejandor"]
            aula = "22"
            maestro = "maestro Luciano rafael"

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
            alumnos = ["mabel", "ana", "dixie", "fernando", "luis", "javier"]
            aula = "11"
            maestro = "maestro diego dueñas"

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
            alumnos = ["miguel", "renata", "azul", "juan", "miguel", "eduardo"]
            aula = "8"
            maestro = "maestro marcos porchas"

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
            alumnos = ["sophia", "samantha", "bryan", "daria", "karla", "julieta"]
            aula = "5"
            maestro = "maestra karen vargas"

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
            alumnos = ["alejandro", "jose", "lucia", "allison", "astrid", "keyla"]
            aula = "19"
            maestro = "maestro enrique enriquez"

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
