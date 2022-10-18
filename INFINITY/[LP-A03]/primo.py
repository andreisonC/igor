#deixei em repetição para facilitar uma correção para n rodar codigo repetidas vezes#

while True:
    n = int(input('Digite um mumero: '))
    p = []
    for a in range(1, n + 1):
        if n % a ==0:
            p.append(a)
        else:
            pass
    if len(p) == 2:
        print(f'O numero {n} é primo')
    else:
        print(f'O numero {n} não é primo')