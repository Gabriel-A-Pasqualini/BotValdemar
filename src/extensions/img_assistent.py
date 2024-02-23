from asyncio import sleep
import os
import threading
import discord
import interactions
import openai
from utils.img import create
from utils.translator import translateToEn
from interactions import Client, Extension, OptionType, slash_option, Embed


with open('../token.txt') as tk:
    token = tk.readlines()[0]

openai.api_key = token

class Image(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.slash_command(
        "gerar-imagem",
        description="Gero uma imagem baseada em um texto!"
    )                                           
    @interactions.slash_option(
        name="ideia",
        description="Sua ideia de imagem",
        required=True,
        opt_type=OptionType.STRING
    )    
    async def img(self, ctx: interactions.SlashContext,ideia):                                    
        
        time = 60

        embed = Embed(
                      color="#3346FF",
                      title=f"{ideia}",
                      description=f"Realizei sua ideia de: {ideia}",                                                 
                    )        

        texToTrans = translateToEn(ideia)
        genImg = threading.Thread(target=create, args=(texToTrans,))

        #message = await ctx.send(f'Esperer {time} seg!')
        message = await ctx.send(embed=embed)

        for i in range(time):    
            if i < 1:
                genImg.start()
            await message.edit(content=f'{i} / {time}') 
            sleep(1)             
            i+1                 

        texToTrans = str(texToTrans).replace(' ', '_')                   

        path = f'./img/{texToTrans}.png'         

        try:
            #embed.images=path                     |
            #await message.edit(embed=embed)       | Não funciona pois espera uma URL

            await ctx.send(file=path)                         

        except Exception as e:

            embed.color="#F90000"
            embed.title="Erro!"
            embed.description=(str(e)+f' C:/Repositorios/BotValdemar/src/img/{texToTrans}.png')
            embed.images="https://cbissn.ibict.br/images/phocagallery/galeria2/thumbs/phoca_thumb_l_image03_grd.png"
            
            await message.edit(embed=embed)               

def setup(client):
    Image(client)