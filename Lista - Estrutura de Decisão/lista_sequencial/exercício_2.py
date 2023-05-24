import math

def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area

raio = float(input("Digite o raio do círculo: "))
area = calcular_area_circulo(raio)

print(f"A área do círculo de raio {raio} é: {area}")
