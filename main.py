import discord
from PIL import Image
import os

import img.py

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello @{message.author.nick}! You are in {message.guild.name}')
        print(f'{message}')


client.run('ODAzMzQwOTgxMzQ4MzM1Njk3.GNzGoD.DgAbp25K6SX-Pwh0diKPoafQfYXs0sC9J59ju8')
