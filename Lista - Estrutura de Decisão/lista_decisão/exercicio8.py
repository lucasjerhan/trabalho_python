quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (quantidade_maxima + quantidade_minima) / 2

if quantidade_atual >= quantidade_media:
    mensagem = "Não efetuar compra"
else:
    mensagem = "Efetuar compra"

print("A quantidade média é:", quantidade_media)
print("Mensagem:", mensagem)
