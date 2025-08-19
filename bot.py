# bot.py
import os
import random

from datetime import datetime

import discord
from discord import app_commands
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
QUOTES = os.getenv('QUOTES')
TEST = os.getenv('TEST')
KASTENA = os.getenv('KASTENA')
LOG = os.getenv('LOG')
intents = discord.Intents.all()
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message_delete(message: discord.Message):
    if bot.user != message.author:
        log_channel = bot.get_channel(int(LOG))
        output = message.content
        output = 'message deleted:\n' + output + '\nauthor:\n' + str(message.author) + '\nchannel:\n' + message.channel.name
        await log_channel.send(output)
        await bot.tree.sync()


@bot.event
async def on_message(ctx):
    if bot.user != ctx.author:
        lower_ctx = ctx.content.lower()

        if 'crazy' in lower_ctx:
            message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
            await message.add_reaction("<:heh:1285699869239152702>")
            await ctx.channel.send('Crazy?\nI was crazy once.')
            await ctx.channel.send('They locked me in a room.\nA rubber room.')
            await ctx.channel.send('A rubber room with rats.\nRats.')
            await ctx.channel.send('Rats make me crazy.')

        # if 'insane' in ctx.content.lower():
        #     await ctx.channel.send('Insane?\nI was insane once.')
        #     await ctx.channel.send('They locked me in a house.\nA cushioned house.')
        #     await ctx.channel.send('A cushioned house with birds.\nBirds.')
        #     await ctx.channel.send('Birds make me insane.')

        if 'luck' in lower_ctx and 'amakiir' in lower_ctx:
            await ctx.channel.send("Sword of Sight, Sword of Sight,\nFights whatever a Sword can fight,")
            await ctx.channel.send("Can it swing, will it land?\nWith Amakiiri luck, no it can’t!")
            await ctx.channel.send("(No need to) watch out!\nHere comes the Sword of Sightttttt!")
        
        if 'pray' in lower_ctx or 'pr*y' in lower_ctx or 'p***' in lower_ctx and 'spray' not in lower_ctx:
            await ctx.channel.send("Thank Ta'La :pray:")

        if 'bagel' in lower_ctx:
            await ctx.channel.send("Bagels? I was bagels once.")
            await ctx.channel.send('They bageled me in a bagel.\nA bagel bagel.')
            await ctx.channel.send('A bagel bagel with bagels.\nBagels.')
            await ctx.channel.send('Bagels make me bagel.')
        
        if 'robot' in lower_ctx:
            await ctx.channel.send("beep boop")

        if 'burn ' in lower_ctx:
            await ctx.channel.send("rah rah gramerca")
        
        if "ta'la" in lower_ctx:
            await ctx.channel.send("Praise Eclyae :pray:")

        if "calloro" in lower_ctx:
            await ctx.channel.send("ALL HAIL THE SUN GOD")

        if "vethri" in lower_ctx:
            await ctx.channel.send("<:get_banned:1381146032678899743>")

        if "heart is a muscle the size of a rat" in lower_ctx:
            await ctx.channel.send("SPONGEBOB SQUAREPANTS")
        
        if "lives in a pineapple under the sea" in lower_ctx:
            await ctx.channel.send("SPONGEBOB SQUAREPANTS")
        
        if "absorbent and yellow and porous is he" in lower_ctx:
            await ctx.channel.send("SPONGEBOB SQUAREPANTS")
        
        if "if nautical nonsense be something you wish" in lower_ctx:
            await ctx.channel.send("SPONGEBOB SQUAREPANTS")
        
        if "then drop on the deck and flop like a fish" in lower_ctx:
            await ctx.channel.send("SPONGEBOB SQUAREPANTS")
        
        if "spongebob squarepants" in lower_ctx:
            await ctx.channel.send("SPONGEBOB SQUAREPANTS\nSPONGEBOB SQUAREPANTS\nSPONGEBOBBBB\nSQUAREPANTSSSS")

        if "jeff" in lower_ctx:
            await ctx.channel.send('the bestest boy')
        
        if "dog" in lower_ctx and "raw" not in lower_ctx:
            await ctx.channel.send('we love goose')
        
        if "vethri" in lower_ctx:
            await ctx.channel.send('wtf dude')

        if "^^vv<><>ba" in lower_ctx:
            await ctx.channel.send('https://discord.gg/udC4Qt3TwF')
    
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
        message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await message.add_reaction("<:stressed:1285652910952284223>")
        await ctx.send('stress reacted!')
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
