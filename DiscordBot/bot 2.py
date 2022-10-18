from PySimpleGUI import PySimpleGUI as sg
import os
from email.message import EmailMessage
from tqdm import tqdm 
from colorama import *
import discord
import os
#usuarios//login





o = os.linesep

sg.theme('BlueMono')
layout = [
    [sg.Text('Token  '), sg.Input(key='Token')],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')], [sg.Button('Sair')]
]

janela = sg.Window('Login', layout)
while True:
        eventos, valores = janela.read()
        if eventos == 'Entrar':
            class MyClient(discord.Client):
                async def on_ready(self):                   
                    print('Developed by @amdre.py')
                    print('Funcionando como: {0}!'.format(self.user))
                    print('|SERVER  | |CONTEUDO     | |AUTOR   ')
                async def on_message(self, message):
                    print('{0.guild}| {0.content} |{0.author}| '.format(message))
                    if message.content == '.regras':
                        await message.channel.send(f'''Olá, as regras do servidor são:
                        {os.linesep}:point_right:1. Respeitar todos igualmente.
                        {os.linesep}:point_right:3. Não gritar nas calls.
                        {os.linesep}:point_right:4. Não enviar pornográfia.
                        {os.linesep}:point_right:5. Não enviar gore.
                        {os.linesep}:point_right:6. Evitar off-topic.
                        {os.linesep}:point_right:7. Usar bot de música somente nos canais de música. {os.linesep}''')
                    
                    elif message.content == '.TikTok':
                        await message.channel.send(f'''{message.author.name}TikTok oficial da SKY {os.linesep} https://www.tiktok.com/@oficial_teamsky {os.linesep} Passa lá :grin:''')
                    
                    
                    elif message.content == '.tiktok':
                        await message.channel.send(f'''{message.author.name} TikTok oficial da SKY {os.linesep} https://www.tiktok.com/@oficial_teamsky {os.linesep} Passa lá :grin:''')
                    
                    
                    elif message.content == '.Rp':
                        await message.author.send(f'''Oi :D, olha o link do server do discord da SKY city: https://discord.gg/qrGSkAMjvR
            digite: **.wl** para ter acesso ao cadastro da White List!
            Qualquer outra duvida digite: **.ajudarp** que te levaremos diretamente para o suporte do server ;D''')
                        await message.channel.send(f'''Salve {message.author.name}, Te mandei uma mensagem no privado, confere lá''')
                    
                    
                    elif message.content == '.rp':
                        await message.author.send(f'''Oi :D, olha o link do server do discord da SKY city: https://discord.gg/qrGSkAMjvR
            digite: **.wl** para ter acesso ao cadastro da White List!
            Qualquer outra duvida digite: **.ajudarp** que te levaremos diretamente para o suporte do server ;D''')
                        await message.channel.send(f'''Salve {message.author.name}, Te mandei uma mensagem no privado, confere lá''')        
                    
                    elif message.content == '.ajudarp':
                        await message.author.send(f'''Fala com eles aqui: <@!251080522401447936>, <@!630931258498613258>, <@!381233152183500802>, <@!987420394732519434> {os.linesep}Eles vão te ajudar <3  ''')
                    
                    
                    elif message.content == '.Ajudarp':
                        await message.author.send(f'''Fala com eles aqui: <@!251080522401447936>, <@!630931258498613258>, <@!381233152183500802>, <@!987420394732519434> {os.linesep}Eles vão te ajudar <3  ''')
                    

                    elif message.content == '.help':
                        await message.channel.send(f'''Oii :) <@!{message.author.id}>
            Para qualquer ajuda personalizada com rp, visite
            👉<#1000053329973481531>👈 e abra um ticket. Qualquer outra ajuda visite: <#1000053332238401567>
            qualquer duvida com bot está aqui:
            ```
.regras
.tiktok
.rp
.ajudarp
.help
.creditos
.staff`
.site
.wl``
''') 

                    elif message.content == '.ajuda':
                        await message.channel.send(f'''Oii :) <@!{message.author.id}>
            Para qualquer ajuda personalizada com rp, visite
            👉<#1000053329973481531>👈 e abra um ticket. Qualquer outra ajuda visite: <#1000053332238401567>
            Qualquer duvida com bot está aqui:
            ```
.regras
.tiktok
.rp
.ajudarp
.help
.creditos
.staff
.site
.wl```
''')
                    

                    elif message.content == '<@910236137631674479>':
                        await message.channel.send(f'''Olá <@!{message.author.id}>, Qualquer duvida com bot está aqui:
            ```
.regras
.tiktok
.rp
.ajudarp
.help
.creditos
.staff
.site
.wl```
''')
                    
                    
                    elif message.content == '.':
                        await message.channel.send(f'''EPA!!! {message.author.name}, esse é meu prefixo''')

                    elif message.content == '.ip':
                        await message.author.send(f'Olá, o ip do server é: {os.linesep}')

                    elif message.content == '.qp':
                        await message.author.send(f'<:gx_quepro:909147516417753128>')

                    elif  message.content == '.wl':
                        await message.author.send(f'OII :D, ainda to esperando link pra por aqui no bot, assim que estiver pronto eu atualizo :D')
                        await message.channel.send(f'Olá <@!{message.author.id}>, te mandei o link lá no privado!')
                    elif message.content =='.creditos':
                        await message.channel.send(f'''Oi :3 <@!{message.author.id}>, bot criado por <@!424190619968339968>
            Insta dele :https://www.instagram.com/amdre.py/ qualquer job ou algo do tipo chama na dm :D''')
                

                    elif message.content =='.staff':
                        await message.author.send('Aqui está o link:  https://forms.gle/B73JiozWFn417wJE9')
                        await message.channel.send(f'Oi , Fala <@!{message.author.id}>, mano temos vagas para staff se quiser entrar so responder esse form que te mandei no privado!')


                    elif message.content == '.site':
                        await message.channel.send(f'''Olá <@!{message.author.id}>, site oficial da SKY team: https://andrezinpy.github.io/TEAM-SKY_SITE/''')

                    elif message.content == '.marcar':
                        await message.channel.send(f'@everyone')

                    elif message.contet == '.zap':
                        await message.channel.send(f'https://wa.me/{message.content}')

                    elif  message.content == '.twitch':
                        await message.channel.send(f'<@!{message.author.id}>, Aqui o link da twtich: https://www.twitch.tv/nordik_team')



                    async def on_menber_join(self, member):
                            guild = member.guild
                            if guild.system_channel is not None:
                                await  message.channel.sed(f'{member.mention} acabou de entrar no {guild.name}, seja bem vindo(a)!{os.linesep} use *.regras* para regras do servidor, ou me marque para menu de comandos!')
                                await guild.system_channel.send(message)







        intents = discord.Intents.default()
        intents.members = True
        client = MyClient(intents=intents)
        client.run(f"{valores['Token']}")