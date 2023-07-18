from asyncio import sleep
import os
import threading
import discord
import interactions
import openai
from utils.img import create
from utils.translator import translateToEn


with open('../token.txt') as tk:
    token = tk.readlines()[0]

openai.api_key = token

class Image(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client


  
    @interactions.slash_command("gerar-imagem",
                                description="Gero uma imagem baseada em um texto!",
                                options=[
                                        interactions.Option(
                                                                name="text",
                                                                description="What you want to say",
                                                                type=interactions.OptionType.STRING,
                                                                required=True,
                                                            ),
                                        ]
                                )                                           
    async def img(self, ctx: interactions.SlashContext,txt: str):                     
        
        time = 70

        print(txt)

        text = 'faça um desenho colorido que represente o sentiemento de qualia do ser humano diante do vasto universo'

        texToTrans = translateToEn(text)
        genImg = threading.Thread(target=create, args=(texToTrans,))

        message = await ctx.send(f'Await {time} sec!')

        for i in range(time):    
            if i < 1:
                genImg.start()
            await message.edit(content=f'{i} / {time-1}!') 
            sleep(1)             
            i+1        
        
        await ctx.send(f'I will send {texToTrans}, now!')

        path = f'./img\{texToTrans}.png'
                
            #while not check_file:
            #    check_file = os.path.isfile(path)
            #    await ctx.send(f'You image is not ready. I will try again...')

        await ctx.send(file=path)

def setup(client):
    Image(client)