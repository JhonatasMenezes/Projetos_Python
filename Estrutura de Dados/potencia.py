def potencia_iterativa(base: int, expoente: int):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado

def potencia_recursiva_linear(base: int, expoente: int):
    if expoente == 0:
        return 1
        return base * potencia_recursiva_linear(base, expoente - 1)



if __name__ == '__main__':
    print(potencia_iterativa(2,10))
    print(potencia_recursiva_linear(2,10))
