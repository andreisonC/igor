import PySimpleGUI as sg
import requests
import os


def tela_inicial():
    sg.theme('LightBlue3')
    layout = [
        [sg.Text('CEP', size = (3, 1)),sg.Input(size=(10,1),key='cep')],
        [sg.Button('Entrar', size=(5,1)), sg.Button('Sair', size=(5,1))]
       
    ]

    return sg.Window('Busca de CEP', layout, finalize=True,size=(280,70))


def tela_principal():
    layout = [
        [sg.Text('Nada')]
    ]

    return sg.Window('Sistema de Cadastros', layout, finalize=True)

tela1, tela2 = tela_inicial(), None

def main():
    event, values = tela1.Read()
    qnt = len(values['cep'])
    if len(values['cep']) !=8:
        sg.popup(f'''Numero de caraceteres invalidos({qnt})!
favor conferir
Programa será finalizado.''')
        tela1.close()
    if event == 'Sair':
        tela1.close()
    elif event == 'Entrar':
        cep = values['cep']
        request = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        address_data = request.json()
    
    if 'erro' not in address_data:
        [sg.popup(f'''cep pesquisado com sucesso!
CEP: {(address_data['cep'])}          
RUA: {(address_data['logradouro'])}       
BAIRRO: {(address_data['bairro'])}       
CIDADE/UF: {(address_data['localidade'])}/{(address_data['uf'])}
DDD: {(address_data['ddd'])}   ''')]
    else:
        sg.popup(f'Erro ao pesquisar CEP!')
        
if __name__=='__main__':
    main()        