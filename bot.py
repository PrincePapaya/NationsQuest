# bot.py
import os
import random

import discord
from discord import app_commands
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
QUOTES = os.getenv('QUOTES')
TEST = os.getenv('TEST')
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

    # if 'insane' in ctx.content.lower():
    #     if bot.user != ctx.author:
    #         await ctx.channel.send('Insane?\nI was insane once.')
    #         await ctx.channel.send('They locked me in a house.\nA cushioned house.')
    #         await ctx.channel.send('A cushioned house with birds.\nBirds.')
    #         await ctx.channel.send('Birds make me insane.')

    if 'luck' in ctx.content.lower() and 'amakiir' in ctx.content.lower():
        if bot.user != ctx.author:
            await ctx.channel.send("Sword of Sight, Sword of Sight,\nFights whatever a Sword can fight,")
            await ctx.channel.send("Can it swing, will it land?\nWith Amakiiri luck, no it can’t!")
            await ctx.channel.send("(No need to) watch out!\nHere comes the Sword of Sightttttt!")
    
    if 'pray' in ctx.content:
        if bot.user != ctx.author:
            await ctx.channel.send("Thank Ta'La :pray:")
    await bot.tree.sync()


@bot.hybrid_command(description = "reacts with :heh:")
async def hehreact(ctx: commands.Context):
    if ctx.message.reference:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await message.add_reaction("<:heh:1285699869239152702>")
        await ctx.send('heh reacted!')
    else:
        await ctx.send("didn't work fool")
    await bot.tree.sync()

@bot.hybrid_command(description="reacts with :stressed:")
async def stressreact(ctx: commands.Context):
    if ctx.message.reference:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await message.add_reaction("<:stressed:1285652910952284223>")
        await ctx.send('stress reacted!')
    else:
        await ctx.send("didn't work fool")
    await bot.tree.sync()

@bot.hybrid_command(description="instantly quote insanity")
async def quote(ctx: commands.Context):
    if ctx.message.reference:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        qc = bot.get_channel(int(TEST))
        await qc.send(message.content)
        await ctx.send('quoted!')
    else:
        await ctx.send("didn't work fool")
    await bot.tree.sync()

@bot.hybrid_command(description="such a nerd")
async def anbennar(ctx: commands.Context):
    await ctx.send("nerd . . .")
    await bot.tree.sync()

@bot.hybrid_command(description= 'sends the bot\'s latency.')
async def ping(ctx: commands.Context):
    await ctx.send(f'Pong! Latency is {bot.latency}')
    await bot.tree.sync()
    

bot.run(TOKEN)
