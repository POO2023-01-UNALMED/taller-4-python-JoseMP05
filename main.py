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
    print(grupo3._grupo)
    print(grupo3._asignaturas == [asignatura1])
    print(grupo3.listadoAlumnos)
    ok = False
    if grupo1._grupo == "grupo predeterminado" and grupo1._asignaturas == [] and grupo1.listadoAlumnos == [] and\
            grupo2._grupo == "Grupo 32" and grupo2._asignaturas == [] and grupo2.listadoAlumnos == [] and \
            grupo3._grupo == "Grupo 23" and grupo3._asignaturas == [asignatura1] and grupo3.listadoAlumnos == [] and\
            grupo4._grupo == "Grupo 12" and grupo4._asignaturas == [
            asignatura1, asignatura2] and grupo4.listadoAlumnos == ["Jaime", "David", "Oswaldo"]:
        ok = True
    print(ok)
