import discord
from discord.ext import commands
from settings import token
from atik import *

intents = discord.Intents.default()
intents.message_content = True

# Botunuzu oluşturun
bot = commands.Bot(command_prefix='!', intents=intents)

# Yardım komutunu oluşturun
@bot.command()
async def yardim(ctx):
    yardim_mesaji = """
    Merhaba! Ben çevre dostu bir Discord botuyum. İşte kullanabileceğiniz komutlar:
    
    !bilgi - Çevre temizliği ve sürdürülebilirlik hakkında bilgi alın.
    !geri_donusum - Geri dönüşüm hakkında ipuçları alın
    !enerji_tasarrufu - Enerji tasarrufu hakkında öneriler alın.
    """
    await ctx.send(yardim_mesaji)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for i in plastik_atik_listesi:
        if i.lower() in message.content.lower():
            await message.channel.send("Plastik atık kutusuna atılmalıdır.\n PET şişeler (örneğin, su şişeleri): Yaklaşık 450 yıl. \n Polistiren (Styrofoam): Binlerce yıl. \n PVC (Polivinil Klorür) malzemeler: Binlerce yıl.  ")
            return

# Bilgi komutunu oluşturun
@bot.command()
async def bilgi(ctx):
    bilgi_mesaji = "Çevre temizliği ve sürdürülebilirlik konusunda bilgi almak için çevre kuruluşlarının web sitelerini ziyaret edebilirsiniz."
    await ctx.send(bilgi_mesaji)
    
bot.run(token)