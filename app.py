import re
from stock import *
import discord
from discord.ext import commands,tasks
from datetime import datetime


bot = commands.Bot(command_prefix='!')
TOKEN = ''

#readin TOKEN
f = open("TOKEN","r")
TOKEN = f.readline()

text_channel_list = []
mycategory = ''





def check():
    global mycategory,text_channel_list
    text_channel_list = []
    text_channel_list_name = []
    for channel in bot.get_all_channels():
        if str(channel.type) == 'text' and channel.category_id == 936150063649030154:
            text_channel_list_name.append(channel.name)
            text_channel_list.append(channel)
            mycategory = channel.category

    # print(text_channel_list)
    return text_channel_list_name


@bot.command()
async def new(ctx, arg):
    global mycategory
    regex = re.compile(r'\d{4,6}')
    if not re.match(regex, arg):
        await ctx.send("not stock!")
    else:
        guilds = await bot.fetch_guilds(limit=150).flatten()
        for guild in guilds:
            text_channel_list_name = check()
            if arg not in text_channel_list_name:
                channel = await guild.create_text_channel(arg)
                await channel.edit(category=mycategory)
                await ctx.send("Done!")
            else:
                await ctx.send("already exit...")

@bot.event
async def on_ready():
    global alarm_time
    print(bot.user)
    print("Bot Online.\n" + "-"*10)


@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def upadtename():
    print("update name")
    r = check()

    for ch in text_channel_list:
        regex = re.compile(r'\d{4,6}')
        if not re.match(regex, ch.name):
            continue
        else:
            stockname = regex.search(ch.name).group()
            print(stockname)
            time = date.today().strftime('%Y-%m-%d')
            after_name = getStockstate(stockname)
            await ch.edit(name=after_name)

upadtename.start()
bot.run(TOKEN)
