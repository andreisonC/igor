from colorama import *
from PySimpleGUI import PySimpleGUI as sg
import time
while True:
    sg.theme('LightBlue3')
    layout = [

        [sg.Text('Digite seu numero de consumidor         '), sg.Input(key='user',size=(4,1))],
        [sg.Text('Quantidade de kwh consumidos no mês'), sg.Input(key='kwh', size=(4,1) )],
        [sg.Combo(['Comercial','Industrial','Residencial'], enable_events=True, key='-SLIDER-')],
        [sg.Button('Calcular')],
]
    janela = sg.Window('Medidor de KWH', layout)


    eventos, valores = janela.read()


    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        j = {valores['user']}
        if {valores['user']} != '0' and valores['kwh'] != '0':
            [sg.popup(f'Bem vindo, numero de consumidor, {j} !',size=(4,1))]
            if valores['-SLIDER-'] == 'Comercial':
                vap = valores['kwh'] * 0.5
                [sg.popup('ismael')]
                print('asdas')
        else:
            [sg.popup('Numero de consumidor não pode ser 0')]




"""def janela_linguagem():
    sg.theme('BlueMono')
    layout = [
        [sg.Text('Choose language')],
        [sg.Combo(['Portugês','English','Français','Español'],key = 'lingage')],
        [sg.Button('Continue')]
    ]




import PySimpleGUI as sg

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 12))

layout = [[sg.Slider(range=(1, 99), resolution=0.4, enable_events=True, orientation='h', key='-SLIDER-')]]
window = sg.Window('Title', layout, finalize=True)

while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    value = values['-SLIDER-']
    print(type(value), value)

window.close()"""