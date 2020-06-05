
if __name__ == '__main__':
    num1 = float(input('Ingresa el numero a usar '))
    while num1 < 20:
        num1 = float(input('El numero debe ser mayor a 20, por favor ingresar de nuevo '))
    result = num1 ** 0.5
    print(f'El resultado es: {round(result,3)}')