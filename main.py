import os
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests

# The channel ID goes here in cid, you can get channel id from devloper mode in discord.
cid = 1159924726295187597

# The token is user token of discord, u need to put it in secrets in the beginning.
token = os.environ['token']
editing = {}
req = requests.get("https://discord.com/api/path/to/the/endpoint")
import time
import random

client = commands.Bot(command_prefix='.')
client._skip_check = lambda x, y: False


@tasks.loop(seconds=0.2)
async def spammer():
    text_channel = client.get_channel(cid)
    # print(text_channel)
    if text_channel != None:
        # words = ["gaeming","om","ap","harry","nato"]
        #print(x)
        num = random.randint(1, 10000000000000000000000000)
        await text_channel.send(num)
        intervals = [2.0, 2.1, 2.2, 2.3, 2.4]
        await asyncio.sleep(random.choice(intervals))


@tasks.loop(seconds=10400)
async def sleeper():
    time.sleep(seconds=1600)
    spammer.start()


#pokes = ['pikachu','charixadd','swellow','pidove',input('option')]
spammer.start()


@client.command()
async def stop(ctx):
    spammer.stop()


@client.command()
async def spam(ctx):
    spammer.start()


keep_alive()
client.run(token, bot=False)