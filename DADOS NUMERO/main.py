import PySimpleGUI as sg
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def janela_linguagem():
    sg.theme('BlueMono')
    layout = [
        [sg.Text('Choose language')],
        [sg.Combo(['Portugês','English','Français','Español'],key = 'lingage')],
        [sg.Button('Continue')]
    ]
    return sg.Window('Choose language', layout=layout,finalize=True)

def janela_numero():
    sg.theme('BlueMono')
    layout =[
        [sg.Text('Digite seu numero:'), sg.Input(key='numero')],
        [sg.Button('Continuar'),sg.Button('Voltar')]
    ]
    return sg.Window('Insira o numero', layout=layout,finalize=True)


janela1,janela2 = janela_linguagem(), None
while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Continue':
        janela2 = janela_numero()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Continuar':
        phone = ((values['numero']))
        phone_ajusted = phonenumbers.parse(phone, 'BR')
        print(phone_ajusted)        
        #geocoder       
        
        local = geocoder.description_for_number(phone_ajusted, 'pt-br')
        print(local)        
        #carrier        
        carrier = carrier.name_for_number(phone_ajusted, 'pt-br')
        print(carrier)
