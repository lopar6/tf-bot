from gc import enable
import os
import random
from typing import Tuple

import discord
from discord import message
from discord import channel
from discord.flags import Intents
from dotenv import load_dotenv

message_options = (
    "Whom the fuk?",
    "New member, who TF is this",
    "Halt. Who tf goes there?",
    "Who to heck?",
    "Whomst is thine?"
)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

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
    global myChannel
    myChannel = client.get_channel(CHANNEL_ID)
    if myChannel is None:
        print("ERROR: channel not found")
    else:
        # await myChannel.send("Who tf am I?")
        print("Who tf am I?")

@client.event
async def on_member_join(member):
    print(f'{member} joined')
    await myChannel.send(getSnarkyMessage())

def getSnarkyMessage() :
    return random.choice(("Who tf?", random.choice(message_options)))

# todo add tuples of options for the bot to say
# todo add random selection each time member joins, then send
client.run(TOKEN)
