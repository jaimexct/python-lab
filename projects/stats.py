def promedio_materias(calificaciones):

    promedios = []

    for materia in calificaciones:

        suma = 0
        contador = 0

        for nota in materia:

            if nota != 0:
                suma += nota
                contador += 1

        if contador > 0:
            promedio = suma / contador
        else:
            promedio = None

        promedios.append(promedio)

    return promedios




