from gc import enable
import os
import random
from typing import Tuple
from google_images_search import GoogleImagesSearch, google_api
import discord
from discord import message
from discord import channel
from discord.flags import Intents
from dotenv import load_dotenv
import uuid

# https://stackoverflow.com/questions/32500498/how-to-make-a-process-run-on-aws-ec2-even-after-closing-the-local-machine

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

# set up google search
GOOGLE_SEARCH_KEY = os.getenv('GOOGLE_SEARCH_KEY')
PROJECT_CX = os.getenv('PROJECT_CX')
google = GoogleImagesSearch(GOOGLE_SEARCH_KEY, PROJECT_CX)

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

# todo add test if on current clan
@client.event
async def on_member_join(member):
    print(f'{member} joined')
    await myChannel.send(getSnarkyMessage())
    if random.randint(1, 2) == 2:
        google.search(search_params=_search_params, path_to_dir='images/', custom_image_name="who-tf")
        with open("images/who-tf.jpg", 'rb') as imageFile:
            file = discord.File(imageFile)
            await myChannel.send('Is this you?', file=file)
        if os.path.exists('images/who-tf.jpg'):
            os.remove('images/who-tf.jpg')

def getSnarkyMessage() :
    # add check for time and asking why someone joined so late
    return random.choice(("Who tf?", random.choice(MESSAGE_OPTIONS)))

# todo idea if a drawer organizer starts typing it interupts them with a .05% chance

# todo replace q "test" with actual queue
_search_params = {
    'q': 'test',
    'num': 1,
    'safe': 'medium',
    'fileType': 'jpg'
}

@client.event
async def on_message(message):
    # if someone says whotf the bot reacts, occationally it replies
    # todo add check if self
    currentChannel = message.channel
    if message.content.lower() in WHO_TF_OPTIONS:
        await message.add_reaction(client.get_emoji(random.choice(EMOJI_ID_OPTIONS)))
        if random.randint(0, 10) == 5:
            await currentChannel.send(random.choice(TF_REPLY_OPTIONS))

client.run(TOKEN)
