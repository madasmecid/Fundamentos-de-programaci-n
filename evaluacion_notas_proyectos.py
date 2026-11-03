def evaluar_proyectos(lista_proyectos):
    resultados = {}
    for alumno in lista_proyectos:
        total = sum(alumno["notas"]) / len(alumno["notas"])
        if total >= 4:
            resultados[alumno["alumno"]]= "aprobado"

        else:
            resultados[alumno["alumno"]]= "reprobado"

    return resultados



def main():

    proyectos = [
        {"alumno": "Marco", "notas": [6.5, 7.0, 6.8]},
        {"alumno": "Lucas", "notas": [3.5, 4.0, 3.8]},
        {"alumno": "Sofia", "notas": [5.0, 6.0, 5.5]}
    ]


    resultados = evaluar_proyectos(proyectos)

    print(resultados)

if __name__=="__main__":
    main()