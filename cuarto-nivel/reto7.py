from math import pi


def run(fig):
    if fig == 1:
        figura = 'círculo'
        radio = float(input('Ingrese el radio del círculo '))
        area = pi * radio ** 2
    
    if fig == 2:
        figura = 'cuadrado'
        lado = float(input('Ingrese la longitud del lado del cuadrado '))
        area = lado **2

    if fig == 3:
        figura = 'triángulo'
        base = float(input('Ingrese la longitud de la base del triangulo '))
        altura = float(input('Ingrese la altura del triangulo '))
        area = base * altura / 2

    print(f'El area del {figura} es {area}')
    


if __name__ == '__main__':
    fig = int(input('''Ingrese el numero de la fiugura a la que le desea calcular el area:
    1 - Círculo
    2 - Cuadrado
    3 - Triángulo
    '''))
    run(fig)