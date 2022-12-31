import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
target = os.getenv('TARGET')
client = commands.Bot()
guild_list = []

@client.slash_command(name="mwquote", guild_ids=guild_list)
async def MWQuote(ctx):
  await ctx.respond("https://media.discordapp.net/attachments/991572180225765447/991572269895798896/unknown.png?width=671&height=671")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return 
  if str(msg.author.id) == target:
    # print("Locked Target!")
    await msg.add_reaction('🇲')
    await msg.add_reaction('🇼')

@client.event
async def on_ready():
  print("Bot is now ready to krab MW!")
  for guild in client.guilds:
    guild_list.append(guild.id)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MW"))

print(token)
client.run(token)