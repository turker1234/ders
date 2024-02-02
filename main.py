import discord
from sifreuretici import *
from settings import token

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$2kere2'):
        await message.channel.send("4")
    elif message.content.startswith('sifre'):
        await message.channel.send("şifreniz = " + gen_pass(int(message.content[5:])))
    elif message.content.startswith('yazitura'):
        await message.channel.send(yazi_tura())
    
    else:
        await message.channel.send(message.content)
    

client.run(token)