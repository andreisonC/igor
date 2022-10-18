from colorama import *
from PySimpleGUI import PySimpleGUI as sg
import time
while True:
    sg.theme('LightBlue3')
    
    layout = []

    tabela = [
        ['H ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'He'],

        ['Li', 'Be', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', ' B', 'C ', 'N ', 'O ', 'F ', 'Ne'],

        ['Na ', 'Mg ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],

        ['K ', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],

        ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe'],
        ['Cs', 'Ba', 'Hf', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Ti', 'Pb', 'Bi', 'Po', 'At', 'Rn'],
        ['Fr', 'Ra', '',  'Rf', 'Db', 'Sg','Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'],
        ['H', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['H', '', '', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb','Lu'],
        ['H', '', '', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'],
    ]

    for linha in range(10):
        coluna1 = []
        for coluna in range(18):
            if (not (coluna > 0 and coluna < 17)) and  (linha == 0):
                coluna1.append(sg.Button(f'{tabela[linha][coluna]}', size=(6, 3), border_width = 0))
            elif (not (coluna > 1 and coluna < 12)) and ((linha == 1) or linha == 2):
                coluna1.append(sg.Button(f'{tabela[linha][coluna]}', size=(6, 3), border_width = 0))
            elif linha == 3 or linha == 4:
                coluna1.append(sg.Button(f'{tabela[linha][coluna]}', size=(6, 3), border_width = 0))
            elif (linha == 5) or (linha == 6):
                if not(coluna == 2):
                    coluna1.append(sg.Button(f'{tabela[linha][coluna]}', size=(6, 3), border_width = 0))
                else:
                    coluna1.append(sg.Button('', size=(6, 3), disabled=True, button_color = 'LightBlue2', border_width = 0))
            elif linha == 7:
                    coluna1.append(sg.Button('', size=(6, 3), disabled=True, button_color = 'LightBlue2', border_width = 0))
            elif linha == 8 or linha == 9:
                if not (coluna < 3):
                    coluna1.append(sg.Button(f'{tabela[linha][coluna]}', size=(6, 3), border_width = 0))
                else:
                    coluna1.append(sg.Button('', size=(6, 3), disabled=True, button_color = 'LightBlue2', border_width = 0))
            else:
                coluna1.append(sg.Button('', size=(6, 3), disabled=True, button_color = 'LightBlue2', border_width = 0))

        layout.append(coluna1)

    
    janela = sg.Window('TABELA PERIODICA', layout, size=(1185,650), background_color='LightBlue2')


    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'ELEMENTO':
        if valores['user'] != '0' and valores['kwh'] != '0':
            [sg.popup(f'Bem vindo, numero de consumidor:', valores['user']+ '!')]
            # if valores[0] == 'Comercial':
            if valores[0] == 'Comercial':
                vap = int(valores['kwh']) * 0.5
                [sg.popup(vap)]
                print('deu ruim')
                print(valores)
        else:
            [sg.popup('Numero de consumidor não pode ser 0')]
            break

# linha1 = []
# coluna2 = []

# for linha in range(10):
#     coluna1 = []
#     for coluna in range(10):
#         coluna1.append('ELEMENTO')

#     linha1.append(coluna1)
