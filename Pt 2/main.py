# main.py
import discord
from discord.ext import commands
import json

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

prefix = config["settings"]["prefix"]
client = commands.Bot(command_prefix=prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.command()
async def ping(ctx):
    await ctx.channel.send("Pog")
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send("The member has been banned from the server")
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send("The member has been kicked from the server")
@client.command()
async def help(ctx):
    await ctx.channel.send("Tutorial Bot Help")
    await ctx.channel.send("I am new here but you can test me out by doing !ping, for admins and moderators you can use !kick and !ban")

client.run(config["token"])