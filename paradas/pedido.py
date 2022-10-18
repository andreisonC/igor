from PySimpleGUI import PySimpleGUI as sg

sg.theme('BlueMono')
layout = [
    [sg.Text('QUER NAMORAR COMIGO?')],
    [sg.Button('SIM'),sg.Button('NÃO')]
]


janela = sg.Window('Login', layout)
while True:
        eventos, valores = janela.read()
        if eventos == 'NÃO':
            [sg.popup('essa n é a resposta >:[')]
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'SIM':
            [sg.popup('Acho bom!')]
            break