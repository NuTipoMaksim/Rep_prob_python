import discord
from discord.ext import commands
import os, random
print(os.listdir('images'))
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'а ты знал, что пластиковые бутылки разлагаются от 400 до 700 лет! а пакеты от 100 до 200 лет! а вот последствия:')
    img_name = random.choice(os.listdir('image'))
    with open(f'image/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTE3ODI3NDA2NTc4MjQxOTQ2Ng.GJogk6.xFJubGiyG2ewfaiqx1zF8witAUAFk1NDBSm4Uo")
