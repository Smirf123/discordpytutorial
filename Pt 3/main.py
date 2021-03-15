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
    embed = discord.Embed()
    embed.add_field(name="Champ", value="Poggers")
    embed.set_footer(text="Memers")
    await ctx.channel.send(embed=embed)
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
    embed=discord.Embed()
    embed.add_field(name="Help", value="Welcome to the help of the tutorial bot")
    embed.add_field(name="kick <@user> <reason>", value="Kicks the user from the server")
    embed.add_field(name="ban <@user> <reason>", value="Bans the user from the server")
    await ctx.channel.send(embed=embed)

client.run(config["token"])