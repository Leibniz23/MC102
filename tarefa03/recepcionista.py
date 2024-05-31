nome = input('Nome do doador(a): ')
idade = int(input('Idade: '))


if 16 <= idade < 18:
    autorizacao = input("Possui documento de autorização (S/N)? ")
    if autorizacao in ['S']:
        print("Doador apto. Encaminhar para a próxima etapa!")
    else:
        print("Doador não atende os requisitos de idade.")

if 18 <= idade < 60:
    print("Doador apto. Encaminhar para a próxima etapa!")

if 60 <= idade <= 69:
    doacao_anterior = input('Já realizou doação anterior (S/N)? ')
    if doacao_anterior in ['S', 's']:
        idade_anterior = int(input("Idade da primeira doação: "))
        if idade_anterior <= 60:
            print("Doador apto. Encaminhar para a próxima etapa!")
        else:
            print("Doador não atende os requisitos de idade.")
    else:
        print("Doador não atende os requisitos de idade.")

if idade < 16 or idade > 69:
    print ("Doador não atende os requisitos de idade.")