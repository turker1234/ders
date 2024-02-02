import discord
from sifreuretici import *
from settings import token

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
words = ["örnek1", "örnek2", "örnek3"]
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for word in words:
        if word in message.content:
            await message.channel.send("Hakaret Uyarısı")
            return
  
    else:
        await message.channel.send(message.content)
    

client.run(token)