from gc import enable
import os
import random
from typing import Tuple

import discord
from discord import message
from discord import channel
from discord.flags import Intents
from dotenv import load_dotenv

MESSAGE_OPTIONS = (
    "Whom the fuk?",
    "New member, who TF is this",
    "Halt. Who tf goes there?",
    "Who to heck?",
    "Whomst is thine?"
)

WHO_TF_OPTIONS = (
    "whotf",
    "who tf",
    "who tf?",
    "who tf?!"
)

TF_REPLY_OPTIONS = (
    "Hey! That's my job!",
    "Nice"
)

EMOJI_ID_OPTIONS = (
    775567355077853194,
    847958237797941248,
    847959550140350507,
    604862449023320082,
    847959736238604324
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
    # add check for time and asking why someone joined so late
    return random.choice(("Who tf?", random.choice(MESSAGE_OPTIONS)))

# if someone says whotf the bot reacts, occationally it replies
# if a drawer organizer starts typing it interupts them with a .05% chance
@client.event
async def on_message(message):
    currentChannel = message.channel
    if message.content.lower() in WHO_TF_OPTIONS:
        await message.add_reaction(client.get_emoji(random.choice(EMOJI_ID_OPTIONS)))
        if random.randint(0, 10) == 5:
            await currentChannel.send(random.choice(TF_REPLY_OPTIONS))

client.run(TOKEN)
