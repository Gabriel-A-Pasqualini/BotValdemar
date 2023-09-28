from asyncio import sleep
import threading
import discord
import interactions
import openai
from utils.translator import translateToEn
from interactions import Client, Embed, Extension, Modal, ModalContext, OptionType, ParagraphText, slash_option
#from chatterbot import Chatterbot
#from chatterbot.trainers import ListTrainer

with open('../token.txt') as tk:
    token = tk.readlines()[0]

openai.api_key = token

class SlashChaty(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    
    @interactions.slash_command("conversar",description="Converso com voce!")                                           
    @interactions.slash_option(
        name="teste",
        description="Sua fala",
        required=True,
        opt_type=OptionType.STRING
    )    
    async def chat(self, ctx: interactions.SlashContext,teste):   

        modal = Modal(
            ParagraphText(label="Teste", custom_id="idteste"),
            title="Teste",
            custom_id="teste"
        )        
        await ctx.send_modal(modal)  
            
        modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)
        msg = modal_ctx.responses["idteste"]

        print(msg)
        
        embed = Embed(
                      color="#3346FF",
                      title="Embed Title",
                      description=f"{teste}", 
                      thumbnail="https://cbissn.ibict.br/images/phocagallery/galeria2/thumbs/phoca_thumb_l_image03_grd.png"                           
                    )               

        try:
            message = await ctx.send(embed=embed)

            embed.color="#FF33F0"
            sleep(2)
            await message.edit(embed=embed) 

        except Exception as e:
            await ctx.send(f"Ocorreu um erro: {str(e)}")

def setup(client):
    SlashChaty(client)