while True:
    salario = float(input('Digite valor que você recebe: '))
    if salario  <= 280:
        total = salario + salario *0.20
    elif salario > 280 and  salario <= 700:
        total = salario + salario * 0.15
    elif salario > 700 and   salario <= 1500:
        total = salario +  salario *0.10
    else:
        total = salario +  salario *0.05
    print(total)