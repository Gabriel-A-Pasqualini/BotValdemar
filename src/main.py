import logging
import asyncio
import os
from interactions import Client, Intents, listen

logging.basicConfig()
cls_log = logging.getLogger("Valdemar")
cls_log.setLevel(logging.ERROR)

with open('../token.txt') as tk:
    token = tk.readlines()[0]

client = Client(intents=Intents.ALL, sync_interactions=True, logger=cls_log)

@listen()
async def on_startup():
    print("Bot ready")
    
def load_extensions():
    for filename in os.listdir('./extensions'):
        if filename.endswith('.py'):
            client.load_extension(f'extensions.{filename[:-3]}')
  
if __name__ == '__main__':
    load_extensions() 
    client.start(token)