from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

if __name__ == "__main__":
    asignatura1 = Asignatura("Vision por Computador")
    asignatura2 = Asignatura("POO", "Salon 503B")

    grupo1 = Grupo()
    grupo2 = Grupo("Grupo 32")
    grupo3 = Grupo("Grupo 23", [asignatura1])
    grupo4 = Grupo("Grupo 12", [asignatura1, asignatura2], [
                   "Jaime", "David", "Oswaldo"])

    ok = False
    if grupo1._grupo == "grupo predeterminado" and grupo1._asignaturas == [] and grupo1.listadoAlumnos == [] and\
            grupo2._grupo == "Grupo 32" and grupo2._asignaturas == [] and grupo2.listadoAlumnos == [] and \
            grupo3._grupo == "Grupo 23" and grupo3._asignaturas == [asignatura1] and grupo3.listadoAlumnos == [] and\
            grupo4._grupo == "Grupo 12" and grupo4._asignaturas == [asignatura1, asignatura2] and grupo4.listadoAlumnos == ["Jaime", "David", "Oswaldo"] and\
            Grupo.grado == "Grado 12":
        ok = True
    print(ok)
    """     asignatura1 = Asignatura("Matematicas")
        asignatura2 = Asignatura("Castellano", "Salon 201")
        grupo1 = Grupo()

        print(asignatura1)
        print(grupo1)
        print(grupo1.grado)

        grupo2 = Grupo("Grupo 5", [], ["Alejandro", "Carlos"])

        grupo3 = Grupo()
        grupo4 = Grupo()
        grupo5 = Grupo()
        grupo3.agregarAlumno("Kelly")
        grupo4.agregarAlumno("Santiago", ["Jaime", "Pedro"])
        grupo5.agregarAlumno("Javier")

        print(grupo3.listadoAlumnos)
        print(grupo4.listadoAlumnos)
        print(grupo5.listadoAlumnos)

        grupo3.listadoAsignaturas(as1="Ciencias", as2="Quimica", as3="Ingles")
        print(len(grupo3._asignaturas))

        Grupo.asignarNombre("Grado 1")
        print(Grupo.grado)
        Grupo.asignarNombre()
        print(Grupo.grado)
    """
