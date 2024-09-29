# bot.py
import os
import random
import nations_quest

import discord
from discord import app_commands
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'Anbennar':
        await message.channel.send('nerd')
    print('done')

@bot.command(name='Anbennar')
async def mimu(ctx):
    await ctx.send('nerd...')

bot.run(TOKEN)