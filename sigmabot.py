# bot created for purpose of learning discord bots
#made by Jason Lin
import random
from random import randint
import discord
import os


from dotenv import load_dotenv
from discord.ext import commands


#seed(20)
#randpenis = randint(0, 10)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="^", intents = intents)
bot.remove_command("help")
#bot = commands.Bot(help_command = None)

@bot.command()
async def ping(ctx):
    await ctx.channel.send('pong! {0}'.format(round(bot.latency,4)) + " ms")

@bot.command()
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
    embed.add_field(name='^ping', value='Returns Pong! along with latency')
    embed.add_field(name = '^penis', value = 'Returns a penis :pensive:')

    await ctx.send(embed = embed)

#@bot.command()
#async def recipe():

@bot.command()
async def info(ctx):
    name = str(ctx.guild.name)
    embed = discord.Embed(title = str(ctx.guild.name) + "Server Information", description = "This is a bot testing server", color = discord.Colour.dark_gold())

    await ctx.send(embed = embed)

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


