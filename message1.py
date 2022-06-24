import pandas as pd
import discord
import asyncio
from discord import Intents
from discord import Embed, File
# from distutils import command
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
import csv
import json
import time
import os.path


token = "OTQ2NzI1ODE5NjUxMzI1OTcy.G_sGOW.uDppI1uEIs6vZ14eci7btQFBt-xRXUnK7gEjaI"
prefix = "-"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)
if os.path.isfile("message.csv"):

    dict_customers = []
    with open('message.csv', 'r',encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, lineterminator='\r')
        for csv_customer in reader:
                
                df = { "title": csv_customer['title'],
                "description": csv_customer['description'], 
                "url": csv_customer['url'],
                "image_url": csv_customer['url'], 
                "color": csv_customer['colour'], 
                "thumbnail" : csv_customer['thumbnail'],
                "authname" : csv_customer['authname'],
                "authurl": csv_customer['authurl'],
                "authlink": csv_customer['authlink'],
                "fieldname": csv_customer['fieldname'],
                "fieldvalue": csv_customer['fieldvalue'],
                "footertext": csv_customer['footertext']}
        
                dict_customers.append(df)
                jsonData = json.dumps(df,indent=2)

    # df['url']= df['url'][4:]
    # df['image_url'] = df['image_url'][4:]
    # df['thumbnail']= df['thumbnail'][4:]
    # df['authurl']= df['authurl'][4:]
    # df['authlink']= df['authlink'][4:]
    color = int(df['color'], 16)  
    os.remove("message.csv")
    @bot.event
    async def on_ready():
        print(f"The bot is online!")
    
    if df['title'] == "":
        print('No message to send')
    else:

        @bot.event
        async def on_ready():
            print(f"The bot is online!")
            channel = bot.get_channel(946758177087709204)
            # await channel.send("API Call")
            embed = Embed(title=df['title'], url=df["url"], description=df['description'], color=color)
            embed.add_field(name=df['fieldname'], value=df['fieldvalue'], inline=False)
            embed.set_author(name=df['authname'], icon_url=df['authurl'])
            embed.set_footer(text=df['footertext'])
            embed.set_thumbnail(url=df['thumbnail'])
            embed.set_image(url=df['image_url'])

            await channel.send(embed=embed)
            print('Message Sent')
else:
    print("Content for Message is not available")

bot.run(token)

# start = time.time()

# while True:
#     time.sleep(1)