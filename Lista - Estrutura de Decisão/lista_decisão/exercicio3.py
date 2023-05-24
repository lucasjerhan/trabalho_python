num_macas = int(input("Digite o número de maçãs compradas: "))

if num_macas < 12:
    custo_total = num_macas * 1.30
else:
    custo_total = num_macas * 1.00

print("O custo total da compra é:", custo_total)