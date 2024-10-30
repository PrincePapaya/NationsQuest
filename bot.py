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
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(ctx):
    if 'crazy' in ctx.content.lower():
        if bot.user != ctx.author:
            await ctx.channel.send('Crazy?\nI was crazy once.')
            await ctx.channel.send('They locked me in a room.\nA rubber room.')
            await ctx.channel.send('A rubber room with rats.\nRats.')
            await ctx.channel.send('Rats make me crazy.')
    await bot.tree.sync()

@bot.hybrid_command()
async def hehreact(ctx: commands.Context):
    message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
    await message.add_reaction("<:heh:1285699869239152702>")
    await ctx.send('heh reacted!')
    await bot.tree.sync()

@bot.hybrid_command()
async def stressreact(ctx: commands.Context):
    message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
    await message.add_reaction("<:stressed:1285652910952284223>")
    await ctx.send('heh reacted!')
    await bot.tree.sync()

@bot.hybrid_command()
async def anbennar(ctx: commands.Context):
    await ctx.send("nerd . . .")
    await bot.tree.sync()

@bot.hybrid_command(description= 'sends the bot\'s latency.')
async def ping(ctx: commands.Context):
    await ctx.send(f'Pong! Latency is {bot.latency}')
    await bot.tree.sync()

bot.run(TOKEN)