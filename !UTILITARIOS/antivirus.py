import os
import time
while True:
    choice = input('''
    
          ╭━─━━─━──━─━━──━─━━─━╮
╭---------|  utilities panel   |----------╮
|         ╰━─━━─━──━─━━──━─━━─━╯          |
╰-----------------------------------------╯
╭-----------------------------------------╮     
| 1  - VERIFICAR VIRUS                    |  
| 2  - INFORMAÇÕES SOBRE A REDE           |
| 3  - PROGRAMAR DESLIGAMENTO             |
| 4  - IP DE UM SITE                      |
| 5  - NJRAT                              |
| 6  - VERIFICADOR DE ARQUIVOS DO SISTEMA |
| 7  - PC INFO                            |
| 8  - IDENTIFICADOR DE PROCESSOS         |
| 9  - EXIBIR CONTEUDO DE UM ARQUIVO      |
| 10 - VERIFICAR VIRUS 2                  |
| E  - SAIR                               |
╰-----------------------------------------╯
>>> ''')
    #VERIFICAR VIRUS
    if choice == '1':
        os.system('scannow')

    #INFORMAÇÕES SOBRE A REDE
    if choice == '2':
        a = os.system('ipconfig')
        for linha in a('\n'):
            if 'Endereço IPv4' in linha:
                print(linha)

    #PROGRAMAR DESLIGAMENTO
    if choice == '3':
        tempo = int(input('''Digite o tempo (em segundos) que deseja desligar o pc: 
        >>> '''))
        os.system(f'shutdown -s -t {tempo}')

    #IP DE UM SITE
    if choice == '4':
        site = input('''Digite o nome do site sem "HTTPS://" ex: google.com 
        >>> ''')
        try:
            os.system(f'ping {site}')
        except:
            print('Algum erro ocorreu, verifique se site está escrito corretamente.')
    
    #NJRAT
    if choice == '5':
        try:
            os.system('start C://Users//andre//Downloads//njRATv0.7d Green Edition.exe')
        except:
            print('Verifique se NJRAT está instalado.')
            time.sleep(1)
    
    #VERIFICADOR DE ARQUIVOS DO SISTEMA
    if choice == '6':
        os.system()
    #PC INFO
    if choice == '7':
        os.system()
    #IDENTIFICADOR DE PROCESSOS
    if choice == '8':
        os.system()
    #EXIBIR CONTEUDO DE UM ARQUIVO
    if choice == '9':
        os.system()
    #VERIFICAR VIRUS 2
    if choice == '10':
        os.system()

    
    if choice == 'E' or choice == 'e':
        print('Saindo... ')
        time.sleep(1)
        quit()