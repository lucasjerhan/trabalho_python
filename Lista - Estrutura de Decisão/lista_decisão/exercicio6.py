valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 < valor2:
    menor = valor1
    maior = valor2
else:
    menor = valor2
    maior = valor1

print("Valores em ordem crescente:", menor, ",", maior)
