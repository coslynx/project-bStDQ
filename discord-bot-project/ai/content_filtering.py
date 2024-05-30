import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Content Filtering Bot is online.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Implement content filtering logic here

client.run('YOUR_DISCORD_BOT_TOKEN')