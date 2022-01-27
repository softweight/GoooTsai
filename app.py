from turtle import position
import discord
import re
from discord.ext import commands

bot = commands.Bot(command_prefix='!') # !Command
TOKEN = ''

#readin TOKEN
f = open("TOKEN","r")
TOKEN = f.readline()

text_channel_list = []
mycategory = ''

def check():
    global mycategory,text_channel_list
    for channel in bot.get_all_channels():
        if str(channel.type) == 'text' and channel.category_id == 936150063649030154:    #
            text_channel_list.append(channel.name)
            mycategory = channel.category

    print(text_channel_list)


@bot.command()
async def new(ctx, arg):
    global mycategory,text_channel_list
	# await ctx.channel.send("got "+arg)
    regex = re.compile(r'\d{4}')
    if not re.match(regex, arg):
        await ctx.send("not stock!")
    else:
        guilds = await bot.fetch_guilds(limit=150).flatten()
        for guild in guilds:
            text_channel_list = []
            check()
            if arg not in text_channel_list:
                channel = await guild.create_text_channel(arg)
                await channel.edit(category=mycategory)
                await ctx.send("Done!")
            else:
                await ctx.send("already exit...")

alarm_time = '23:33'#24hrs
channel_id = '51599XXXXX5036697'

@bot.event
async def on_ready():
    print('Bot Online.')

alarm_time = '23:33'

async def time_check():
    await bot.wait_until_ready()
    while not bot.is_closed:
        now = bot.strftime(bot.now(), '%H:%M')
        channel = bot.get_channel(channel_id)
        messages = ('Test')
        if now == alarm_time:
            
            time = 90
        else:
            time = 1


bot.loop.create_task(time_check())


bot.run(TOKEN)