import os
import threading
from time import sleep
import discord
from discord.ext import commands
from utils.img import create
from utils.translator import translateToEn

with open('../token.txt') as tk:
    token = tk.readlines()[0]


intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
#client = discord.Client(command_prefix='/', intents=intents)
bot = commands.Bot(command_prefix='/',intents=intents)



@bot.slash_command(name="first_slash", guild_ids=[337790268818587659]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  
    if message.author == client.user:
        return
    

    if message.content.startswith('hello'):        
        message = await message.channel.send(f'Hello @{message.author.nick}! You are in {message.guild.name}')
        print(message)

    if message.content.startswith('img'):
        time = 70
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
        
        while not check_file:
            check_file = os.path.isfile(path)
            await message.channel.send(f'You image is not ready. I will try again...')

        await message.channel.send(file=discord.File(path))
        
client.run(token)
bot.run(token)