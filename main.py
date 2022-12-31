import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
target = os.getenv('TARGET')
client = commands.Bot()

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return 
  if str(msg.author.id) == target:
    print("Locked Target!")
    await msg.add_reaction('🇲')
    await msg.add_reaction('🇼')

@client.event
async def on_ready():
  print("Bot is now ready to krab MW!")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MW"))

print(token)
client.run(token)