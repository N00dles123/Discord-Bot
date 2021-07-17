# bot created for purpose of learning discord bots
#made by Jason Lin
import random
from random import randint
import discord
import os
import json
import requests
import urllib.request, urllib.parse, urllib.error




from dotenv import load_dotenv
from discord.ext import commands




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
TENOR = os.getenv('TENOR_KEY')

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="^", intents = intents)
bot.remove_command("help")


@bot.command()
async def ping(ctx):
    await ctx.channel.send('pong! {0}'.format(round(bot.latency,4)) + " ms")

@bot.command()
async def penis(ctx):
    userid = ctx.message.author.id
    name = bot.get_user(userid)
    random.seed(userid)
    value = round(random.uniform(1,15),2)
    penis = "8"
    for x in range(int(value)):
        penis += "="
    penis += "D"
    embed = discord.Embed(title = f"{ctx.message.author}'s"+ " Penis Length is "+ str(value) + " :eggplant:  ", description = penis, colour = discord.Colour.green())
    await ctx.send(embed = embed)


@bot.command()
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name ='Help')
    embed.add_field(name = '^info', value ='Returns information about the server such as amount of members')
    embed.add_field(name='^ping', value='Returns Pong! along with latency')
    embed.add_field(name = '^penis', value = 'Returns a penis :pensive:')
    embed.add_field(name = '^gif <argument>', value = 'returns a gif based on what argument is')

    await ctx.send(embed = embed)

#command generates gifs based on what arg is
#gifs are from the tenor api and not for profit
@bot.command()
async def gif(ctx, arg):
    lmt = 30
    search_term = str(arg)
    r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, TENOR, lmt))
    if r.status_code == 200:
        top_30gifs = json.loads(r.content)
        value = randint(0, lmt - 1)
        url = top_30gifs['results'][value]['media'][0]['gif']['url']
        embed = discord.Embed(title = f"result for {search_term}: ", description = "", colour = discord.Colour.blurple())
        embed.set_image(url = url)
        await ctx.channel.send(embed = embed)
    else:
        top_8gifs = None


#command gives server info
@bot.command()
async def info(ctx):
    name = str(ctx.guild.name)
    embed = discord.Embed(title = str(ctx.guild.name) + "Server Information", description = "This is a bot testing server", color = discord.Colour.dark_gold())
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = "Owner", value = str(ctx.guild.owner))
    embed.add_field(name = "Server ID", value = str(ctx.guild.id))
    embed.add_field(name = "Region", value = str(ctx.guild.region))
    embed.add_field(name = "Member Count", value = str(ctx.guild.member_count)) 

    await ctx.send(embed = embed)

#command generates recipe
#@bot.command()
#async def recipe(ctx, arg):


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild: \n'
        f'{guild.name}(id: {guild.id})'
        )
    print(bot.user.id)
    await bot.change_presence(activity = discord.Game('Clash of Clans'), status = discord.Status.dnd)



@bot.event
async def on_member_join(member):
    await member.send(f'Hi {member.name}, Welcome to this bot test server!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! :partying_face:')
    if 'fuck you' in message.content.lower():
        await message.channel.send('fuck you too! :middle_finger:')
    await bot.process_commands(message)


bot.run(TOKEN)
