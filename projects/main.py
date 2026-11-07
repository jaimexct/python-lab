from stats import promedio_materias


materias = [
    "Cálculo Diferencial",
    "Álgebra",
    "Geometría Analítica",
    "Metodología de la Programación"
]

calificaciones = [
    [86, 92, 43, 0],
    [83, 100, 0, 0],
    [58, 0, 0, 0],
    [100, 100, 0, 0]
]

promedios = promedio_materias(calificaciones)

for i in range(len(materias)):

    if promedios[i] is not None:
        print(f"{materias[i]}: {promedios[i]:.0f}")
    else:
        print(f"{materias[i]}: Sin calificaciones")
