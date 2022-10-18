dhora = float(input('Digite quanto você cobra por hora: '))
hora = float(input('Quantas horas você trabalhou: '))
val_hora = dhora * hora
ir = val_hora * -0.05
inss = val_hora * -0.10
sind = val_hora * -0.03
fgts = val_hora * -0.11
ir1 = ir*(-1)
inss1 = inss*(-1)
sind1 = sind*(-1)
fgts1 = fgts*(-1)
total = ir1 + inss1+ sind1
sal_liqu = val_hora - total 
print(f'Salario brutos: {val_hora}')
print(f'IR(5%) = R${ir1}')
print(f'INSS(10%) = R${inss1}')
print(f'SINDICATO(3%) = R${sind1}')
print(f'FGTS(11%) = R${fgts1}')
print(f'Total de descontos = R${total}')
print(f'Salario liquido: R${sal_liqu}')
