from gc import enable
import os
import asyncio
from typing import Tuple

import discord
from discord import message
from discord import channel
from discord.flags import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

myChannel = None

@client.event
async def on_ready():
    await client.wait_until_ready()
    print(f'{client.user} has connected to Discord!')
    # ! add channel id number here
    # make sure to enable dev mode on discord
    myChannel = client.get_channel(888455189609201727)
    if myChannel is None:
        print("ERROR: channel not found")
    else:
        await myChannel.send("hello")

# todo fix this to see all new members
@client.event
async def on_member_join(member):
    await myChannel.send("who tf?")


# todo add tuples of options for the bot to say
# todo add random selection each time member joins, then send


client.run(TOKEN)