import discord
from discord.ext import commands
import json, random, asyncio

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

#偵錯-私訊問題
@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.PrivateMessageOnly):
        await ctx.send("DM me '&rps' to use it.")

#embed-bot的使用教學
@bot.command()
async def hi(ctx):
    await ctx.send("hihi")
    print("embed")
    embed = discord.Embed(title="使用教學", color=0x58b2dc)
    embed.set_author(name="by sakana", url="https://github.com/yuxinLatenT/discordbot")
    embed.add_field(name="&ping", value="回傳bot的延遲", inline=0)
    embed.add_field(name="&lots", value="抽籤", inline=0)
    embed.add_field(name="&team", value="身份組", inline=0)
    embed.add_field(name="&rps", value="猜拳", inline=0)
    await ctx.send(embed=embed)
    
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
    print("lots")

#骰子
@bot.command()
async def dice(ctx):
    x = random.randint(1, 6)
    await ctx.send(x)

#數字炸彈
@bot.command()
async def n_and_b(ctx):
    print("boooon!!")
    
#猜數字遊戲(bulls&cows)
@bot.command()
async def b_and_c(ctx):
    await ctx.send("hihi")
    
#猜拳
@bot.command()
@commands.dm_only()
async def rps(ctx):
    print("rock_paper_scissors")
    await ctx.send("剪刀(2)、石頭(0)、布(5)選一個!")

#身分組
@bot.command()
async def team(ctx):
    await ctx.send("請在此訊息下方新增反映貼圖以取得身分組:")
    jdata["start_team"] = 1
    print("team", jdata["start_team"])
    await asyncio.sleep(60*3) #身份組取得的權限持續3分鐘
    jdata["start_team"] = 0
    print("team", jdata["start_team"])
    
#身分組取得-按圖示
@bot.event
async def on_raw_reaction_add(payload):
    print("reaction", jdata["start_team"])
    if(payload.emoji.name in jdata and jdata["start_team"]):
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