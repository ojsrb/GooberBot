import os

import discord
from discord import Intents
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name='ping')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}")
    ephemeral = True

@client.tree.command(name='insult')
async def insult(interaction: discord.Interaction, user: discord.User):
    if user.id == 800898653820551168:
        await interaction.response.send_message("You cannot insult my papa!", ephemeral=True)
    else:
        await interaction.channel.send(f"{user.id} is a big meanie!")


@client.tree.command(name='papa')
async def papa(interaction: discord.Interaction):
    if interaction.user.id == 800898653820551168:
        await interaction.response.send_message("You are my papa!")
    else:
        await interaction.response.send_message("You are not my papa! o.n. is my papa!")

@client.tree.command(name='say')
async def say(interaction: discord.Interaction, message: str):
    if interaction.user.id == 800898653820551168:
        await interaction.response.send_message("sending message...", ephemeral=True)
        await interaction.channel.send(message)

    else:
        await interaction.response.send_message("You cant do that!", ephemeral=True)

client.run(TOKEN)
