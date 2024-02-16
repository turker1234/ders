import discord
from discord.ext import commands
from atik import *

intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Hoşgeldiniz {member.mention} to {guild.name} büyük harflerle bir atık ismi giriniz.'
            await guild.system_channel.send(to_send)

    
    async def on_message(self, message):
        print(message.content)
        if message.author == client.user:
            return
        for i in plastik_atik_listesi:
            if i.lower() in message.content.lower():
                await message.channel.send("Plastik atık kutusuna atılmalıdır.\n PET şişeler (örneğin, su şişeleri): Yaklaşık 450 yıl. \n Polistiren (Styrofoam): Binlerce yıl. \n PVC (Polivinil Klorür) malzemeler: Binlerce yıl.  ")
                return
    
        else:
            await message.channel.send(message.content)
        
intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run("MTIwMjMwMzUxMDYwODM2MzU4Mg.GXDSns.jo6H6pe6jjJ0ueH-apD3c5GOSbGDyRsfElSXlg")