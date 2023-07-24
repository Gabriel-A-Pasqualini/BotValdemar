from asyncio import sleep
import threading
import interactions
import openai
from utils.translator import translateToEn
from interactions import Client, Extension, OptionType, slash_option
#from chatterbot import Chatterbot
#from chatterbot.trainers import ListTrainer

with open('../token.txt') as tk:
    token = tk.readlines()[0]

openai.api_key = token

class Chaty(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.slash_command("conversar",description="Converso com voce!")                                           
    @interactions.slash_option(
        name="conversar",
        description="Sua fala",
        required=True,
        opt_type=OptionType.STRING
    )    
    async def chat(self, ctx: interactions.SlashContext,ideia):                             
        await ctx.send(f'Você disse: {ideia}')        
        await ctx.send(f'Vasco da gama!')

def setup(client):
    Chaty(client)