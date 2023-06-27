from time import sleep
import os
import discord
from PIL import Image
from img import create

with open('../token.txt') as tk:
    token = tk.readlines()[0]

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

    if message.content.startswith('$img'):
        time = 20
        imagem = message.content.split('img ')[1]

        await message.channel.send(f'I will gen your image based on {imagem}, but await {time} sec!')

        create(imagem)
        #sleep(time)        
        await message.channel.send(f'I will send {imagem}, now!')
        await message.channel.send(file=discord.File(f'./img\{imagem}.png'))
      
client.run(token)