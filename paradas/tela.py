import PySimpleGUI as sg

def tela_principal():
    layout = [
        [sg.Button('NADA')]
    ]

    return sg.Window('Nada', layout)



tela = tela_principal()