signo = ['Capricornio','Aquario','Peixes','Aries','Touro','Gemeos','Cancer','Leão','Virgem','Libra','Escorpião','Sargitario']
final = [20,19,20,20,21,21,22,22,22,22,22,21]
mes = int(input('Seu mês de nascimento: '))
dia = int(input('Dia que nasceu: '))

mes = mes - 1
if dia > final[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print('Seu signo é :',signo[mes])