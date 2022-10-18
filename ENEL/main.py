import PySimpleGUI as sg
from pytube import YouTube
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

path = input({values['caminho']})
yt = YouTube({values['link']})
result = {
    'title': yt.title,
    'views': yt.views,
    'duration': yt.length,
    'avaliating': yt.rating,
}
print(result)
yr = yt.streams.get_highest_resolution()
print('Video downloading...')
yr.download(path)
print('Video downloaded successfully!')