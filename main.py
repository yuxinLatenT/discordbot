import discord
from discord.ext import commands
import json
import random

with open("setting.json", mode="r", encoding="utf-8") as setting:
    jdata = json.load(setting)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="&", intents=intents)

#告知bot已上線
@bot.event
async def on_ready():
    print('Ready!')

@bot.command()
async def hi(ctx):
    await ctx.send("hihi")

#embed-bot的使用教學

#回傳bot的延遲
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}ms")

#抽籤
@bot.command()
async def lots(ctx):
    x = random.randint(0, 7)
    sign = list(jdata["lot"])
    await ctx.send(sign[x])

#身分組取得
@bot.command()
async def team(ctx):
    await ctx.send("請在此訊息下方新增反映貼圖已取得身分組:")
    

#身分組取得-按圖示
@bot.event
async def on_raw_reaction_add(payload):
    if(payload.emoji.name in jdata):
        guild = bot.get_guild(payload.guild_id)
        role = guild.get_role(jdata[payload.emoji.name])
        user = guild.get_member(payload.user_id)
        await user.add_roles(role)

#身分組移除-取消圖示
@bot.event
async def on_raw_reaction_remove(payload):
    if(payload.emoji.name in jdata):
        guild = bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        role = guild.get_role(jdata[payload.emoji.name])
        await user.remove_roles(role)

#分隊指令-身分組
@bot.command()
async def game_r(ctx):
    ctx.send()

#分隊指令-名字
@bot.command()
async def game_n(ctx):
    print("game_n")
    await ctx.send("輸入:人數、組數")
    #await 

    #ctx.send()



#分隊程式
    """
    決定哪些人要參加
        bot發一則訊息
        點特定貼圖的人獲得身分組
    隨機分組
        有身分組的人列入欲分隊的名單
        隨機分隊
    """
#gamemode 
"""
@bot.event
async def on_message(ctx):
    if(ctx.content=="rick"):
        await ctx.channel.send("roll!")
    else:
        pass    
"""
bot.run(jdata["Token"])