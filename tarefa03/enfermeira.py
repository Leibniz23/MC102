doadores = int(input())
n_doadores_m = 0
n_doadores_f = 0
peso_f = 0
peso_m = 0

for n in range(1,doadores+1):
    peso, sexo, gravidez, doacoes, dias_doacao = input().split()
    peso = float(peso)
    doacoes = int(doacoes)
    dias_doacao = int(dias_doacao)

    if peso >= 50:
        if sexo == "F":
            if gravidez == "N":
                if doacoes <= 3:
                    if dias_doacao > 90:
                        n_doadores_f += 1
                        peso_f += peso
                        
        if sexo == "M":
            if doacoes <= 4:
                if dias_doacao > 60:
                    n_doadores_m += 1
                    peso_m += peso

peso_medio = (peso_f + peso_m)/(n_doadores_f + n_doadores_m)

print("Número de doadores aptos do sexo M:", n_doadores_m)
print("Número de doadores aptos do sexo F:", n_doadores_f)
print("Peso médio de doadores aptos: ", f"{peso_medio:.1f}")


