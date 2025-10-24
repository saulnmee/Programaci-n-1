class Curso:
    def __init__(self, nombre: str, aula: str, instructor: str):
        self.nombre = nombre
        self.aula = aula
        self.instructor = instructor
        self.alumnos = []

    def agregar_alumno(self, alumno: str):
        if alumno and alumno not in self.alumnos:
            self.alumnos.append(alumno)
            print(f"Alumno '{alumno}' agregado al curso '{self.nombre}'.")
        elif alumno in self.alumnos:
            print(f"El alumno '{alumno}' ya está inscrito en el curso '{self.nombre}'.")
        else:
            print("Nombre de alumno inválido.")

    def eliminar_alumno(self, alumno: str):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print(f"Alumno '{alumno}' eliminado del curso '{self.nombre}'.")
        else:
            print(f"El alumno '{alumno}' no está inscrito en el curso '{self.nombre}'.")

    def mostrar_info_curso(self):
        print("\n--- Información del curso ---")
        print(f"Curso: {self.nombre}")
        print(f"Aula: {self.aula}")
        print(f"Instructor: {self.instructor}")
        print("Alumnos inscritos:")
        if not self.alumnos:
            print("- (ninguno)")
        else:
            for alumno in self.alumnos:
                print(f"- {alumno}")
        print("------------------------------\n")

    def modificar(self, nuevo_nombre: str = None, nueva_aula: str = None, nuevo_instructor: str = None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nueva_aula:
            self.aula = nueva_aula
        if nuevo_instructor:
            self.instructor = nuevo_instructor
        print(f"Información del curso '{self.nombre}' actualizada.")


class CursosItson:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, nombre: str, aula: str, instructor: str):
        nuevo = Curso(nombre, aula, instructor)
        self.cursos.append(nuevo)
        print(f"Curso '{nombre}' creado y agregado a la lista.")

    def listar_cursos(self):
        if not self.cursos:
            print("No hay cursos registrados.")
            return
        print("\n--- Lista de cursos ---")
        for idx, curso in enumerate(self.cursos, start=1):
            print(f"{idx}. {curso.nombre} (Aula: {curso.aula}, Instructor: {curso.instructor}, Alumnos: {len(curso.alumnos)})")
        print("------------------------\n")

    def buscar_curso(self, nombre: str):
        for curso in self.cursos:
            if curso.nombre.lower() == nombre.lower():
                return curso
        return None

    def menu(self):
        while True:
            print("Elija una opción:")
            print("1. Agregar curso")
            print("2. Listar cursos")
            print("3. Buscar y mostrar curso")
            print("4. Agregar alumno a un curso")
            print("5. Eliminar alumno de un curso")
            print("6. Modificar curso")
            print("7. Eliminar curso")
            print("8. Salir")

            opcion = input("Seleccione una opción (1-8): ").strip()

            if opcion == "1":
                nombre = input("Ingrese el nombre del curso: ").strip()
                aula = input("Ingrese el aula del curso: ").strip()
                instructor = input("Ingrese el instructor del curso: ").strip()
                if nombre:
                    self.agregar_curso(nombre, aula, instructor)
                else:
                    print("El nombre del curso no puede estar vacío.")

            elif opcion == "2":
                self.listar_cursos()

            elif opcion == "3":
                nombre = input("Ingrese el nombre del curso a buscar: ").strip()
                curso = self.buscar_curso(nombre)
                if curso:
                    curso.mostrar_info_curso()
                else:
                    print("Curso no encontrado.")

            elif opcion == "4":
                nombre = input("Ingrese el nombre del curso donde agregar alumno: ").strip()
                curso = self.buscar_curso(nombre)
                if curso:
                    alumno = input("Ingrese el nombre del alumno a agregar: ").strip()
                    curso.agregar_alumno(alumno)
                else:
                    print("Curso no encontrado.")

            elif opcion == "5":
                nombre = input("Ingrese el nombre del curso donde eliminar alumno: ").strip()
                curso = self.buscar_curso(nombre)
                if curso:
                    alumno = input("Ingrese el nombre del alumno a eliminar: ").strip()
                    curso.eliminar_alumno(alumno)
                else:
                    print("Curso no encontrado.")

            elif opcion == "6":
                nombre = input("Ingrese el nombre del curso a modificar: ").strip()
                curso = self.buscar_curso(nombre)
                if curso:
                    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{curso.nombre}'): ").strip()
                    nueva_aula = input(f"Nueva aula (Enter para mantener '{curso.aula}'): ").strip()
                    nuevo_instructor = input(f"Nuevo instructor (Enter para mantener '{curso.instructor}'): ").strip()
                    curso.modificar(nuevo_nombre or None, nueva_aula or None, nuevo_instructor or None)
                else:
                    print("Curso no encontrado.")
            
            elif opcion == "7":
                print("eliminar un curso")
                nombre = input("Ingrese el nombre del curso a eliminar: ").strip()
                curso = self.buscar_curso(nombre)
                if curso:
                    self.cursos.remove(curso)
                    print("Curso eliminado correctamente.")
                else:
                    print("Curso no encontrado.")

            elif opcion == "8":
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    gestor = CursosItson()
    gestor.menu()
