from math import pi

if __name__ == '__main__':
    radio = float(input('Ingresa el radio de la base cilindro '))
    altura = float(input('Ingresa la altura del cilindro '))
    vol = pi * radio ** 2 * altura
    print(f'El volumen del cilindro es: {vol}')