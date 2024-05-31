alimentos = int(input())
lista_alimentos = []
total_prot = 0
total_gordura = 0
total_carbo = 0
nut_ideal= [140,210,56]

for n in range(alimentos):
    nome, proteinas, carbo, gordura = input().split()
    proteinas = float(proteinas)
    carbo = float(carbo)
    gordura = float(gordura)
    vetor_entrada = nome, proteinas, carbo, gordura
    lista_alimentos.append(vetor_entrada)

cafe = input().split()
almoco = input().split()
jantar = input().split()
refeicoes = [cafe,almoco,jantar]

for ref in refeicoes:
    for alimento in ref:
        for alimento_lista in lista_alimentos:
            if alimento_lista[0] == alimento:
                total_prot += alimento_lista[1]
                total_carbo += alimento_lista[2]
                total_gordura += alimento_lista[3]


if nut_ideal[0]<total_prot:
    print(f"{total_prot-nut_ideal[0]:.1f}","gramas de proteína em excesso")
elif nut_ideal[0]>total_prot:
    print(f"{nut_ideal[0]-total_prot:.1f}","gramas de proteína em falta")
else:
    print("Quantidade ideal de proteínas")

if nut_ideal[1]<total_carbo:
    print(f"{total_carbo-nut_ideal[1]:.1f}","gramas de carboidrato em excesso")
elif nut_ideal[1]>total_carbo:
    print(f"{nut_ideal[1]-total_carbo:.1f}","gramas de carboidrato em falta")
else:
    print("Quantidade ideal de carboidratos")

if nut_ideal[2]<total_gordura:
    print(f"{total_gordura-nut_ideal[2]:.1f}","gramas de gordura em excesso")
elif nut_ideal[2]>total_gordura:
    print(f"{nut_ideal[2]-total_gordura:.1f}","gramas de gordura em falta")
else:
    print("Quantidade ideal de gorduras")
