

def obtener_aprobados (notas, nota_minima):
    aprobados = []

    for i in range(len(notas)):
        if notas [i] >= nota_minima:
            aprobados.append(notas[i])

    return aprobados


def calcular_promedio(aprobados):
    promedio = sum(aprobados) / len(aprobados)

    return promedio



def main():

  notas = [3.5, 6.0, 2.0, 5.5, 4.0, 1.5]
  nota_minima = 4.0


  aprobados = obtener_aprobados(notas, nota_minima)

  promedio = calcular_promedio(aprobados)


  print (aprobados)

  print (f"{promedio:.2f}")



if __name__ == "__main__":
    main()