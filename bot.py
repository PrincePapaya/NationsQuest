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

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'crazy' in message.content:
            await message.channel.send('hmm.')
            await client.send_message(message.channel, 'Crazy?')
            await client.send_message(message.channel, 'I was crazy once.')
            await client.send_message(message.channel, 'They locked me in a room.')
            await client.send_message(message.channel, 'A rubber room.')
            await client.send_message(message.channel, 'A rubber room with rats.')
            await client.send_message(message.channel, 'Rats.')
            await client.send_message(message.channel, 'Rats make me crazy.')
    await client.process_commands(message)

@bot.event
async def on_message(ctx):
    if 'crazy' in ctx.content:
        if bot.user != ctx.author:
            await ctx.channel.send('Crazy?')
            await ctx.channel.send('I was crazy once.')
            await ctx.channel.send('They locked me in a room.')
            await ctx.channel.send('A rubber room.')
            await ctx.channel.send('A rubber room with rats.')
            await ctx.channel.send('Rats.')
            await ctx.channel.send('Rats make me crazy.')
    await bot.tree.sync()

@bot.hybrid_command()
async def anbennar(ctx):
    await ctx.send("nerd . . .")
    await bot.tree.sync()

@bot.hybrid_command(description= 'sends the bot\'s latency.')
async def ping(ctx: commands.Context):
    await ctx.send(f'Pong! Latency is {bot.latency}')
    await bot.tree.sync()

bot.run(TOKEN)