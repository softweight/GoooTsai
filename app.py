from turtle import position
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!') # !Command
TOKEN = ''

#readin TOKEN
f = open("TOKEN","r")
TOKEN = f.readline()

# simple ping pong
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content == 'ping':
#         await message.channel.send('pong')


async def on_ready():
    print('Login in : ', bot.user)

@bot.command()
async def new(ctx, arg):
	# await ctx.channel.send("got "+arg)
    guilds = await bot.fetch_guilds(limit=150).flatten()
    print(guilds)
    for i in guilds:
        channel = await i.create_text_channel(arg)
        await channel.edit()

bot.run(TOKEN)