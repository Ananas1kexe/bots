import disnake
import random

from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix = "!", intents=intents, activity=disnake.Game("MADE BY ANANAS1K TEAM PINE X"))


@bot.event
async def on_ready():
    print(f"bot {bot.user} ready")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
    
@bot.slash_command(description="random number")
async def rand(ctx):
    a = random.randint(1,100)
    await ctx.send(a)

@bot.slash_command(description="rando1m number")
async def math(ctx, number1: int, number2: int, sign):
    if sign == "+":
        c = number1 + number2
        await ctx.send(c)
    elif sign == "-":
        c = number1 - number2
        await ctx.send(c)
    elif sign == "*":
        c = number1 * number2
        await ctx.send(c)
    elif sign == "/":
        c = number1 / number2
        if number1 == 0:
            await ctx.send("на ноль делить нельзя гений")
            return
        else:
            await ctx.send(c)
    else:
        await ctx.send("Возможно вы указали не правельный знак действия")
    
    


bot.run('TOKEN')