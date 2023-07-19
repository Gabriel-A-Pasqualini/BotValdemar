from asyncio import sleep
import os
import threading
import discord
import interactions
import openai
from utils.img import create
from utils.translator import translateToEn
from interactions import Client, Extension, OptionType, slash_option


with open('../token.txt') as tk:
    token = tk.readlines()[0]

openai.api_key = token

class Image(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.slash_command("gerar-imagem",
                                description="Gero uma imagem baseada em um texto!"
                                )                                           
    @interactions.slash_option(
        name="ideia",
        description="Sua ideia de imagem",
        required=True,
        opt_type=OptionType.STRING
    )    
    async def img(self, ctx: interactions.SlashContext,ideia):                     
        
        time = 100

        print(ideia)

        texToTrans = translateToEn(ideia)
        genImg = threading.Thread(target=create, args=(texToTrans,))

        message = await ctx.send(f'Esperer {time} seg!')

        for i in range(time):    
            if i < 1:
                genImg.start()
            await message.edit(content=f'{i} / {time}') 
            sleep(1)             
            i+1                        

        path = f'./img\{texToTrans}.png'

        #check_file = os.path.isfile(path)                
        #while not check_file:            
        #    await ctx.send(f'Sua imagem ainda não esta ponta...')
        #    sleep(5)

        await ctx.send(f'Vou enviar dua ideia de: {ideia}')
        await ctx.send(file=path)

def setup(client):
    Image(client)