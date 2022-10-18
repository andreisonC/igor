nome = input('Digite seu nome: ')
idade = int(input('Digite que ano você nasceu: '))
prova = 2022 - idade
if prova >= 18:
    print(f'Olá{nome}, você tem {idade} anos e é de maior')
else:
    print(f'Olá{nome}, você tem {idade} anos e é de menor ')
