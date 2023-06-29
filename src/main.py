import os
import threading
from time import sleep
import discord
from img import create
from translator import translateToEn

with open('../token.txt') as tk:
    token = tk.readlines()[0]

intents = discord.Intents.default()
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
        time = 41
        text = message.content.split('img ')[1]

        texToTrans = translateToEn(text)
        genImg = threading.Thread(target=create, args=(texToTrans,))
        message = await message.channel.send(f'Await {time} sec!')

        sleep(3)

        for i in range(time):    
            if i < 1:
                genImg.start()
            await message.edit(content=f'{i} / {time-1}!') 
            sleep(1)             
            i+1        
        await message.channel.send(f'I will send {texToTrans}, now!')

        path = f'./img\{texToTrans}.png'
        check_file = os.path.isfile(path)

        while not check_file:
            await message.channel.send(f'You image is not ready. I will try again...')

        await message.channel.send(file=discord.File(path))

        os.remove(path)
        
client.run(token)
