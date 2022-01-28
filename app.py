import re
import twstock
from discord.ext import commands,tasks

bot = commands.Bot(command_prefix='!')    #change your prefix what you like

#readin TOKEN
TOKEN = ''
f = open("TOKEN","r")
TOKEN = f.readline()
MYCATEGORYID = 936150063649030154    #check your ID in your server or use None 

#self function
def getStockstate(name):
    stock = twstock.realtime.get(name)
    openprice = twstock.Stock(name).price[-2]
    aftername = name
    # print(openprice)
    if stock['success']:
        newprice = float(stock["realtime"]["latest_trade_price"])
        # print(newprice)
        if newprice >= openprice:
            aftername = f"{name}🔴{newprice}"
        else:
            aftername = f"{name}🟢{newprice}"
        aftername = aftername.replace(".","_")
    return aftername

def check():
    global mycategory,text_channel_list
    textChannel = []
    textChannelName = []
    mycategory = ""
    for channel in bot.get_all_channels():
        if str(channel.type) == 'text' and channel.category_id == MYCATEGORYID:
            textChannelName.append(channel.name)
            textChannel.append(channel)
            mycategory = channel.category
    # print(text_channel_list)
    return textChannel,textChannelName,mycategory


#Command Block
@bot.command()
async def new(ctx, arg):
    global mycategory
    regex = re.compile(r'\d{4,6}')
    if not re.match(regex, arg):
        await ctx.send("not stock!")
    else:
        guilds = await bot.fetch_guilds(limit=150).flatten()
        for guild in guilds:
            textChannel,textChannelName,myCategory = check()
            if arg not in textChannelName:
                channel = await guild.create_text_channel(arg)
                after_name = getStockstate(arg)
                await channel.edit(name=after_name,category=myCategory)
                await ctx.send("Done!")
            else:
                await ctx.send("already exist...")

#Event Block
@bot.event
async def on_ready():
    global alarm_time
    print(bot.user)
    print("Bot Online.\n" + "-"*10)

@tasks.loop(seconds = 30) # repeat after every 30 seconds
async def upadtename():
    print("update name")
    textChannel,textChannelName,myCategory = check()

    for ch in textChannel:
        regex = re.compile(r'\d{4,6}')
        if not re.match(regex, ch.name):
            continue
        else:
            stockname = regex.search(ch.name).group()
            # time = date.today().strftime('%Y-%m-%d')
            after_name = getStockstate(stockname)
            await ch.edit(name=after_name)


#main
def main():
    upadtename.start()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()