import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def joke(ctx):
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        data = response.json()
        joke_text = f"{data['setup']} ... {data['punchline']}"
        await ctx.send(joke_text)
    except Exception as e:
        await ctx.send(f"Failed to fetch joke: {e}")

# Paste your Discord bot token here:
TOKEN = "MTM3ODcwMzc5MTQ1MjQ1NTAwMw.G5oi8g.ulODQgMvjCzy0DEQc_DeOpPefRmh1AZCPwPcG8"

bot.run(TOKEN)