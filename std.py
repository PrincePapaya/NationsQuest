import os

import discord
from discord import app_commands
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
STD = int(os.getenv('STD'))

async def boom(ctx):
    has_it = discord.utils.get(ctx.author.roles, id=STD)
    if has_it:
        await ctx.channel.send("hardy har har")
        await ctx.author.remove_roles(has_it)