from PySimpleGUI import PySimpleGUI as sg
import requests
from colorama import *
import time


def main():
    while True:
        sg.theme('LightBlue3')
        layout = [
        
            [sg.Text('Digite o CEP que de       '), sg.Input(key='user',size=(4,1))],
            [sg.Text('Quantidade de kwh consumidos no mês'), sg.Input(key='kwh', size=(4,1) )],
            [sg.Combo(['Comercial','Industrial','Residencial'], enable_events=True, key='-SLIDER-')],
            [sg.Button('Calcular')],
]   
        janela = sg.Window('Medidor de KWH', layout)
    
    
        eventos, valores = janela.read()
    
        a = {valores['user']}
        if eventos == sg.WINDOW_CLOSED:
            break
        else:
            cep = input(f'Digite o CEP: {Fore.GREEN}')
            print(f'{Fore.WHITE}')
            if len(cep) !=8:
                print(f'{Fore.WHITE}Quantidade de numero invalidos: {Fore.RED}{cep}{Fore.WHITE}')
                main()
            request = requests.get(f'https://viacep.com.br/ws/{a}/json')
            address_data = request.json()
            if 'erro' not in address_data:
                print(f'''

         --------------------
    +----|   {Fore.GREEN}CEP ENCONTRADO{Fore.WHITE} |----+
    |    --------------------    |
    +----------------------------+

    | CEP: {Fore.GREEN}{(address_data['cep'])}{Fore.WHITE}          
    | RUA: {Fore.GREEN}{(address_data['logradouro'])}{Fore.WHITE}       
    | BAIRRO: {Fore.GREEN}{(address_data['bairro'])}{Fore.WHITE}       
    | CIDADE/UF: {Fore.GREEN}{(address_data['localidade'])}/{(address_data['uf'])}{Fore.WHITE}
    | DDD: {Fore.GREEN}{(address_data['ddd'])}   {Fore.WHITE}             
    +========================+
    ''')   
            else:
                print(f'CEP não encontrado: {Fore.RED}{cep}{Fore.WHITE}')

            continar = int(input(f'''Desejeja realizar uma nova consulta?
    1- {Fore.GREEN}Continuar{Fore.WHITE}
    2- {Fore.RED}Sair{Fore.WHITE}
    '''))
            if continar == 1:
                main()
            else:
                print('Saindo...')
if __name__=='__main__':
    main()

    #by andre :D#