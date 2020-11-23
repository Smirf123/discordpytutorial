# main.py
import discord
from discord.ext import commands
import json

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

prefix = config["settings"]["prefix"]
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.command()
async def ping(ctx):
    await ctx.channel.send("Pog")

client.run(config["token"])