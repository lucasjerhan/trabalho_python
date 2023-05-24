nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))

media = (nota1 + nota2) / 2

if media >= 6:
    resultado = "aprovado"
else:
    resultado = "reprovado"

print("A média do aluno é:", media)
print("O aluno está", resultado)
