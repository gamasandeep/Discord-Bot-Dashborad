import streamlit as st
import pandas as pd
import discord
import asyncio
from discord import Intents
from discord import Embed, File
from distutils import command
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

token = "OTgwMjY1NjEyMDk1OTQyNzU4.GXSLAD.B3qX4iQHlm8FksbCnSEtQ-D3fNzR0p0K4b5GNU"
prefix = "-"

intents = discord.Intents.all()

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"The bot is online!")