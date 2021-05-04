## Runs in Linux via: python kultTarotBot.py
## Requires Python > 3.4
## Bot needs to be given message read and send permissions on the Discord server.
## Need to install the discord.py API wrapper (e.g., via: pip install discord.py)

import os
import random
import discord
import all_moves

# Read Discord token from env var
TOKEN = os.environ['DISCORD_BOT_TOKEN']

## Define variables here...

sep = ' '
gap = ''

moves = all_moves.moves

help='''
# Como usar:

!movimento ? - exibe esta mensagem
!movimento help - exibe esta mensagem
!movimento ajuda - exibe esta mensagem
!movimento info - exibe informações do Bot
!movimento xxx - realiza um movimento xxx
!movimento xxx -1 - realiza um movimento xxx com um modificador negativo de -1
!movimento xxx +2 - realiza um movimento xxx com um modificador positivo de +2

O gatilho para ativar o movimento pelo bot pode ser:
- !m
- !movimento

Movimentos:
- Use o nome completo do movimento (em minúsculas, sem espaços) ao jogar.
  Por exemplo, para jogar 'Observar uma Situação' com um bônus de +2, use:
  !m observarumasituacao +2
- Atalhos estão disponíveis para os movimentos mais usados (veja abaixo).
  Por exemplo, para jogar 'Evitar Ferimento' com um bônus de +1, use:
  !m ef +1

# Atalhos de movimentos:
- Evitar Dano (ed): jogue + Reflexos
- Suportar Ferimento (sf): jogue + Fortitude - Dano (+ Armadura)
- Manter o Sangue-frio (msf): jogue + Força de Vontade
- Agir Sob Pressão (asp): jogue + Sangue-frio
- Participar do Combate (pdc): jogue + Violência
- Influenciar um PdM (ipm): jogue + Carisma
- Influenciar um Pj (ipj): jogue + Carisma
- Ver Através da Ilusão (vai): jogue + Alma
- Ler uma Pessoa (lup): jogue + Intuição
- Observar uma Situação (oas): jogue + Percepção
- Investigar (inv): jogue + Razão
- Ajudar ou Atrapalhar (aoa): jogue + Atributo
- Movimento fora do padrão (mov): jogue + Modificador
'''

## Get discord connection
client = discord.Client()

## Define an event so that Bot can read messages
@client.event
async def on_message(message):

    ## Bot info
    guildList='\n- '.join(map(lambda g: g.name, list(client.guilds)))
    info=f'''
# KultMoveBotBr
Código-fonte disponível em: https://github.com/paulodiovani/kult-move-bot-ptbr
Atualmente rodando em {len(list(client.guilds))} servidores Discord:
- {guildList}
'''

    ## Converts move command to lowercase, making it
    ## case insensitive
    message.content=message.content.lower()

    ## Respond if user sends "!movimento" or its short aliases
    triggers = ('!movimento ', '!m ')
    if message.content.startswith(triggers):

        ## Split into into "!move", the type of Move to undertake, the modifier (if any), and a comment (if any).
        bits = message.content.split(" ")

        dice = '```md\n'
        if len(bits)==1:
            dice += 'Favor, espeficique um Movimento (ou "!movimento ?" para ajuda)'

        if len(bits)>1:
            if bits[1] in ["?", "help", "ajuda"]:
                dice += help

            elif bits[1] in ["info"]:
                dice += info

            elif bits[1] in ["/", "s", "search", "p", "procurar"]:
                search = bits[2]
                if len(search) <= 3:
                    dice += 'A busca precisa ter 4 ou mais caracteres.'
                else:
                    moveList = list(filter(lambda m: search in m, list(moves)))

                    if len(moveList) >= 1:
                        moveListStr = '\n- '.join(moveList)
                        dice += f'Movimentos similares a "{search}":\n- {moveListStr}'
                    else:
                        dice += f'Nenhum movimento similar a "{search}" encontrado.'

            elif bits[1] not in moves:
                dice += 'Favor, espeficique um Movimento (ou "!movimento ?" para ajuda)'

            elif bits[1] in moves:
                roll = [random.randint(1,10), random.randint(1,10)]

                #Instead of going by case to case basis, think about how easy it is to add moves now
                options = moves[bits[1]]

                result = roll[0] + roll[1]
                mod = ''

                if len(bits) > 2:
                    mod = [' ',list(bits[2])[0],' ',list(bits[2])[1],' ']
                    mod = gap.join(mod)
                    if list(bits[2])[0]=="+":
                        result = result + int(list(bits[2])[1])
                    elif list(bits[2])[0]=="-":
                        result = result - int(list(bits[2])[1])

                if result < 10:
                    outcome = options[3]
                elif result > 14:
                    outcome = options[1]
                else:
                    outcome = options[2]

                dice += options[0]
                dice += "\nRESULTADO: "
                dice += str(roll[0])
                dice += " + "
                dice += str(roll[1])
                dice += mod
                dice += " = "
                dice += str(result)
                dice += "\nEFEITO: "
                dice += outcome

        dice += '```'

        ## Send message to channel
        await message.channel.send(dice)

## Write login details locally (i.e., on linux box where bot code is running)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Kult: !movimento ? para ajuda"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("Installed on",len(list(client.guilds)), "guilds:")
    for s in list(client.guilds):
        print("- " + s.name)
    print('------')

## Run Bot on Discord server
client.run(TOKEN)
