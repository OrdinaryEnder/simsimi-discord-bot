import discord
import json
from simsimi import simsimi
from dotenv import load_dotenv
import os

load_dotenv()
channel = os.getenv("CHANNEL")
token = os.getenv("TOKEN")
intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged In as {client.user}")
    await client.change_presence(activity=discord.Game(name="With Simsimi!"))

@client.event
async def on_message(message):
  content = message.content
  if message.author.bot:
    return

  channel_id = message.channel.id
  channel_id = str(channel_id)
  
  if channel_id in channel:
    response = simsimi(content)
    await message.reply(response, mention_author=False)

  if isinstance(message.channel, discord.DMChannel):
    response = simsimi(content)
    await message.reply(response, mention_author=False)

client.run(token)
