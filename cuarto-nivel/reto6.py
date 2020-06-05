
if __name__ == '__main__':
    num1 = float(input('Ingresa el dividendo '))
    num2 = float(input('Ingresa el divisor '))
    entero = num1 // num2
    residuo = num1 % num2
    print(f'El resultado de dividir {num1} entre {num2} es {entero} y sobra {residuo}')