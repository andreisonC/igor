import discord
import os
import random
ban = ('<@!1002661492249862154>','<@!320263468689129473>')
user = ('<@!970819055407759421>','<@!381233152183500802>','<@!424190619968339968>','<@!338058688147488778>','<@!902220473792872468>','<@!492826354400755733>','<@!939997966129848351>',' <@!244891392793509888>','<@!968267545746477056>','<@!892969342818471937>','<@!778405660818669598>','<@!424362515732889602>','<@!630931258498613258>')
class MyClient(discord.Client):
    async def on_ready(self):                   
        print('Developed by @amdre.py')
        print('Funcionando como: {0}!'.format(self.user))
        print('|SERVER  | |CONTEUDO     | |AUTOR   ')
    async def on_message(self, message):
        print('{0.guild}| {0.content} |{0.author}| '.format(message))
        if message.content == '.0923b1293812hn3':
            await message.channel.send(f'''Olá, as regras do servidor são:
            {os.linesep}:point_right:1. Respeitar todos igualmente.
            {os.linesep}:point_right:3. Não gritar nas calls.
            {os.linesep}:point_right:4. Não enviar pornográfia.
            {os.linesep}:point_right:5. Não enviar gore.
            {os.linesep}:point_right:6. Evitar off-topic.
            {os.linesep}:point_right:7. Usar bot de música somente nos canais de música. {os.linesep}''')
        
        elif message.content == '.TikTok':
            await message.channel.send(f'''{message.author.name} TikTok oficial da NODIK {os.linesep} https://www.tiktok.com/@nordik_team {os.linesep} Passa lá :grin:''')
        
        
        elif message.content == '.tiktok':
            await message.channel.send(f'''{message.author.name} TikTok oficial da NODIK {os.linesep} https://www.tiktok.com/@nordik_team {os.linesep} Passa lá :grin:''')
        
        
        elif message.content == '.Rp':
            await message.author.send(f'''Oi :D, olha o link do server do discord da SKY city: https://discord.gg/qrGSkAMjvR
digite: **.wl** para ter acesso ao cadastro da White List!
Qualquer outra duvida digite: **.ajudarp** que te levaremos diretamente para o suporte do server ;D''')
            await message.channel.send(f'''Salve {message.author.name}, Te mandei uma mensagem no privado, confere lá''')
        
        
        elif message.content == '.rp':
            await message.author.send(f'''Oi :D, olha o link do server do discord da NORDIK city: https://discord.gg/qrGSkAMjvR
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
.staff
.site
.wl
.blusa
```
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
.wl
.blusa```
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
.wl
.blusa```
''')
        
        


        elif message.content == '.ip':
            await message.author.send(f'Olá, o ip do server é: {os.linesep}connect grupocancun.ddns.net')

        elif message.content == '.qp':
            await message.author.send(f'<:gx_quepro:909147516417753128>')

        elif  message.content == '.wl':
            await message.author.send(f'OII :D, ainda to esperando link pra por aqui no bot, assim que estiver pronto eu atualizo :D')
            await message.channel.send(f'Olá <@!{message.author.id}>, te mandei o link lá no privado!')
        elif message.content =='.creditos':
            await message.channel.send(f'''Oi :3 <@!{message.author.id}>, bot criado por <@!424190619968339968>
Insta dele :https://www.instagram.com/amdre.py/ qualquer job ou algo do tipo chama na dm :D''')
    

        elif message.content =='.staff':
            await message.channel.send(f'Oi , Fala <@!{message.author.id}>, mano temos vagas para staff se quiser entrar so responder esse form que te mandei no privado!')
            await message.author.send('https://forms.gle/tN6jJvpZzZ35E9rt5')

        elif message.content == '.site':
            await message.channel.send(f'''Olá <@!{message.author.id}>, site oficial da NORDIK: https://andrezinpy.github.io/TEAM_NORDIK/''')

        elif message.content == '.marcar':
            await message.channel.send(f'@everyone')

        elif message.content == '.calvo':
            await message.channel.send(f'Ei <@!{message.author.id}>,Brunão mandou tirar :(')
            await message.channel.send('<:pou:1004795208506036335>')

        elif message.content == '.regras':
            await message.channel.send(f'''Ei <@!{message.author.id}>, aqui as regras:
            # Por favor, leia atentamente as regras listadas abaixo:

 ```PROIBIDO FAZER DIVULGAÇÕES SEM CONTATAR UM STAFF OU O BRUNO !!!! - SE FIZER LEVARÁ PUNIÇÃO!! 

1. Seja educado(a), respeito é bom e de graça, use e abuse dele!
2. O servidor do discord tem disponibilidade para qualquer pessoa, indiferentemente da etnia, sexualidade, etc.
3. A utilização do chat de dúvidas deverá ser apenas e unicamente para sanar dúvidas.
4. A utilização do batepapo deverá ser apenas e unicamente para conversas entre jogadores.
5. É proibido ofender qualquer jogador ou administrador no discord.
6. Assédio é estritamente proibido.
7. Proibido fazer postagens racistas, homofóbicas e com qualquer NSFW.
8. Evite spam! Mensagens repetidas atrapalham o chat, por favor, tenha bom senso!
9. Por favor, não grite. Evite o uso excessivo do CAPS LOCK.
10. Links externos não são permitidos, se necessário a postagem de algum link, encaminhar por pv para um moderador.
11. É Extremamente Proibido QualQuer Compartilhamento De PornoGrafia, seja Imagem , Foto, Vídeo, Link, Etc...
12. É proibido a divulgação de outro Discord ou Servidor, caso alguém fique enviando spam sobre outro servidor/discord em seu privado por favor entre em contato com algum ADM/MOD o mais rapido possivel!
13. Quem setar rank falso será PUNIDO!```''')


        elif message.content == '.1':
            await message.channel.send('<#1003784994042425545>')

        elif message.content == '.podcast':
            await message.channel.send('Olá gente, @everyone, desculpa está de marcando novamente, mas estamos on no NORDIKAST! entra ai: <#1004793113870598316>')

        elif message.content == '.ban':
            await message.channel.send(random.choice(ban))

        elif message.content == '.blusa':
            await message.channel.send(f'''<@!{message.author.id}>
Aqui está o link: https://forms.gle/oPW1QLTgoQFvF9Jy7''')

        elif  message.content == '.twitch':
            await message.channel.send(f'<@!{message.author.id}>, Aqui o link da twtich: https://www.twitch.tv/nordik_team')

        while message.author == 'andre games#2005':
                await message.channel.send(f'{message.author} teste')
                break
        

        async def on_menber_join(self, member):
                guild = member.guild
                if guild.system_channel is not None:
                    await  message.channel.sed(f'{member.mention} acabou de entrar no {guild.name}, seja bem vindo(a)!{os.linesep} use *.regras* para regras do servidor, ou me marque para menu de comandos!')
                    await guild.system_channel.send(message)







intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run('OTEwMjM2MTM3NjMxNjc0NDc5.GsjkVY.ezysuvxEKbAsu1y9jZnYd-t-6og0LDeCMxfKgM')