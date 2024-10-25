import disnake
import random


from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents, status=disnake.Status.online, activity=disnake.Game("hi"))

@bot.event
async def on_ready():
    print(f"bot {bot.user} ready")
            
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel:  # Если системный канал не равен None
        embed = disnake.Embed(description=f"{member.mention} Добро пожаловать на **{guild.name}**!", color=disnake.Color.green())
        await guild.system_channel.send(embed=embed)
        
@bot.event
async def on_member_remove(member):
    guild = member.guild
    if guild.system_channel:  # Если системный канал не равен None
        embed = disnake.Embed(description=f"{member.mention} Покинул сервер **{guild.name}**!", color=disnake.Color.red())
        await guild.system_channel.send(embed=embed)



@bot.slash_command(description="kick user")
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, user: disnake.User, reason: str = "Нет причины"):
    guild = user.guild
    if guild.system_channel:  # Если системный канал не равен None
        embed = disnake.Embed(description=f"{ctx.author.mention} кикнул **{user.mention}**!", color=disnake.Color.red())
        await guild.system_channel.send(embed=embed)
        
    await user.kick(reason=reason)
    
@bot.slash_command(description='ban users')
@commands.has_permissions(ban_members=True, administrator=True)
async def unban(interaction: disnake.ApplicationCommandInteraction, user: disnake.User, reason: str = "Нет причины"):
    guild = user.guild
    if guild.system_channel:  # Если системный канал не равен None
        embed = disnake.Embed(description=f"{interaction.author.mention} забанил **{user.mention}**!", color=disnake.Color.red())
        await guild.system_channel.send(embed=embed)
        
    await interaction.guild.ban(user, reason=reason)

# @bot.slash_command(description='unban users')
# @commands.has_permissions(ban_members=True, administrator=True)
# async def unban(interaction: disnake.ApplicationCommandInteraction, user: disnake.User, reason: str = "Нет причины"):
#     guild = user.guild
#     if guild.system_channel:  # Если системный канал не равен None
#         embed = disnake.Embed(description=f"{interaction.author.mention} разбанил **{user.mention}**!", color=disnake.Color.red())
#         await guild.system_channel.send(embed=embed)
        
#     await interaction.guild.unban(user, reason=reason)
    
    
    
    
@bot.slash_command(description="calc")
async def math(ctx, num1:  int, num2:  int, sign: str = commands.Param(choices=["+", "-", "*", "/"])):
    if sign == "+":
        a =  int(num1) + int(num2)
        await ctx.send(f"Ваш ответ: {a}")
    elif sign == "-":
        b =  int(num1) - int(num2)
        await ctx.send(f"Ваш ответ {b}")
    elif sign == "*":
        c =  int(num1) * int(num2)
        await ctx.send(f"Ваш ответ {c}")
    elif sign == "/":
        d =  int(num1) / int(num2)
        if num1 != 0:
            d = num1 / num2
        else:
            await ctx.send("Division by zero is not allowed!")
            return
        await ctx.send(f"Ваш ответ {d}")
        
    else:
        await ctx.send("Ошибка попробуйте еще раз а")

@bot.slash_command(description="Рандомное число от 0 до 100") #ready
async def rand(ctx, num1: int = 0, num2: int = 100):
    num = random.randint(num1, num2)
    await ctx.send(f'Рандомное число: {num}')
#game
@bot.slash_command(description="game number")
async def game(ctx, number, num1: int = 0, num2: int = 100):
    b = random.randint(num1, num2)
    await ctx.send(f'выберите число от: {num1} до: {num2}')
    if number == b:
        await ctx.send("вы выиграли")
    else:
        await ctx.send(f'вы проиграли было загадоно число  {b}')


bot.run('YOUR TOKEN BOT')