# bot.py
import os
import random

import discord
from discord import app_commands
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')
intents = discord.Intents.all()
intents.message_content = True
prefix = '/'
bot = commands.Bot(command_prefix=prefix, intents=intents)
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.hybrid_command()
async def anbennar(ctx):
    await ctx.send("nerd . . .")
    await bot.tree.sync()

@bot.hybrid_command(description= 'sends the bot\'s latency.')
async def ping(ctx: commands.Context):
    await ctx.send(f'Pong! Latency is {bot.latency}')
    await bot.tree.sync()

bot.run(TOKEN)