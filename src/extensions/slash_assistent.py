import interactions
import openai


with open('../token.txt') as tk:
    token = tk.readlines()[0]

openai.api_key = token

class SlashTeste(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client


    @interactions.slash_command("hello", description="Só testa o comando!")
    async def hello(self, ctx: interactions.SlashContext):
        await ctx.send("Eu gosto do vasco!")

def setup(client):
    SlashTeste(client)