from discord.ext import commands
import discord

BOT_TOKEN = "MTM5MzMxODY2NTUzMjk5NzY5Mg.GYtKyx.GKQQH2Q0SIGsZ2uKGYNtMbK0cAlSG2SWM9RafA"
CHANNEL_ID = 1391223596205998130
KEY_PHRASE = "froze"

bot = commands.Bot(command_prefix ="!", intents=discord.Intents.all())

intents = discord.Intents.default()
intents.message_content = True
client  = discord.Client(intents = intents)

# @bot.event
# async def on_ready():
#     print("Hello! Alarm bot is ready!")
#     channel = bot.get_channel(CHANNEL_ID)
#     await channel.send("Hello! Alarm bot is ready!")

# @bot.command()
# async def destroyed(ctx):
#     await ctx.send("GETTING RAIDED BRO")

@client.event
async def on_ready():
    print(f"🤖 Logged in as {client.user}")

@client.event
async def on_message(message):
    if(KEY_PHRASE.lower() in message.content.lower()):
        print(message.content)
        print("GETTING RAIDED")

    # if message.author == client.user:
    #     return

    # if message.channel.id != CHANNEL_ID:
    #     return

    # elif KEY_PHRASE.lower in message.content.lower():
    #     await message.channel.send("ALERT GETTING RAIDED")

# bot.run(BOT_TOKEN)
client.run(BOT_TOKEN)