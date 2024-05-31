alimentos_favoritos = input().split()
dias = int(input())
cardapio_geral = []
for cardapio in range(dias):
    cardapio_do_dia = input().split()
    cardapio_geral.append(cardapio_do_dia)

dia_com_alimentos_geral = []

for cardapio_dia in cardapio_geral:
    dia_com_alimentos = [cardapio_dia[0]]
    dia_com_alimentos_geral.append(dia_com_alimentos)
    for cardapio in cardapio_dia:
        for alimento in alimentos_favoritos:
            if cardapio == alimento:
                dia_com_alimentos.append(cardapio)

maior_soma = 0
cardapio_1 = 0
cardapio_2 = 0

for i in range(len(dia_com_alimentos_geral)):
    for j in range(i+1,len(dia_com_alimentos_geral)):
        soma = len(dia_com_alimentos_geral[i])
        for k in dia_com_alimentos_geral[j]:
            if k not in dia_com_alimentos_geral[i]:
                soma += 1
        if soma > maior_soma:
            maior_soma = soma 
            cardapio_1 = i
            cardapio_2 = j

print("Juan pode comer", maior_soma - 2, "alimentos diferentes")
print(*dia_com_alimentos_geral[cardapio_1])
print(*dia_com_alimentos_geral[cardapio_2])

