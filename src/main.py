import asyncio
from time import sleep
import os
import discord
from img import create
from translator import translateToEn

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

        message = await message.channel.send(f'Hello @{message.author.nick}! You are in {message.guild.name}')
        
    if message.content.startswith('$img'):
        time = 60
        text = message.content.split('img ')[1]

        texToTrans = translateToEn(text)

        message = await message.channel.send(f'I will gen your image based on {text}, but await {time} sec!')

        gen = False
        gen = create(texToTrans)
        
        while not gen:        
            for i in range(time):    
                await message.edit(content=f'await {i} sec!')
                sleep(1)               
                i+1
        
        await message.channel.send(f'I will send {texToTrans}, now!')
        await message.channel.send(file=discord.File(f'./img\{texToTrans}.png'))
            
client.run(token)