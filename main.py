def minimum_operations(t, cases):
    results = []
    
    for i in range(t):
        l, r, x = cases[i][0]
        a, b = cases[i][1]
      
      
        if b < l or b > r:
            results.append(-1)
        else:
            if (a - l) % x == 0:
                diff = abs(a - b)
                operations = diff // x
                results.append(operations)
            else:
                results.append(-1)
    
    return results


def main():
    t = int(input("Ingrese el número de casos de prueba (no menor a 1, no mayor a 10^4): "))
    if t < 1 or t > 10**4:
        print("El valor ingresado para t es inválido. Por favor, inténtelo de nuevo.")
        return

    cases = []

    for i in range(t):
        l, r, x = map(int, input("Ingrese l, r y x para el caso {}: ".format(i + 1)).split())
        a, b = map(int, input("Ingrese a y b para el caso {}: ".format(i + 1)).split())
        cases.append([(l, r, x), (a, b)])

    results = minimum_operations(t, cases)

    print("Resultados:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()