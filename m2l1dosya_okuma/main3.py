import os
import requests
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
print(os.listdir('images'))
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    liste = os.listdir('images')
    sayi = random.randint(1,10)
    if sayi <=5:
        index = 0
    elif sayi <=8:
        index= 1
    else:
        index=2
        
    with open('images/'+liste[index], 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
# # # # def get_duck_image_url():    
# # # #     url = 'https://random.dog/woof.json'
# # # #     res = requests.get(url)
# # # #     data = res.json()
# # # #     return data['url']


# # # # @bot.command('duck')
# # # # async def duck(ctx):
# # # #     '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
# # # #     image_url = get_duck_image_url()
# # # #     await ctx.send(image_url)
    
bot.run("")