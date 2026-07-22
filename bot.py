import discord
import random

# intents variable stores the permissions of the bot
intents = discord.Intents.default()
# Enable the permission to read message content
intents.message_content = True
# Create a bot and pass the intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/help'):
        await message.channel.send("What do you want")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send("somthing is worng")
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

WELCOME_CHANNEL_ID = 1438992076283969651  # Replace with your channel ID

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"🎉 Welcome {member.mention}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("/coinflip heads") or message.content.startswith("/coinflip tails"):
        result = random.choice(["heads", "tails"])
        await message.channel.send(f"The coin landed on {result}!")
    elif message.content.startswith("/coinflip"):
            await message.channel.send("Please use /coinflip heads or /coinflip tails.")
                  
            
    elif message.content.startswith("/add"):
        
        try:
            _, left, right = message.content.split()
            left = int(left)
            right = int(right)
            
            if left == 6 and right == 7:
                await message.channel.send("67!!!")
            else:
                   await message.channel.send(left + right)
        except:
            await message.channel.send("Usage: /add 5 7")
    
    elif message.content.startswith("/roll"):
        try:
            _, dice = message.content.split()
            rolls, limit = map(int, dice.split("d"))
            result = ", ".join(
                str(random.randint(1, limit))
                for _ in range(rolls)
            )
            await message.channel.send(result)
        except Exception:
            await message.channel.send("Format has to be NdN! Example: /roll 2d6")
            
    elif message.content.startswith('$help'):
        await message.channel.send("What do you want")
    elif message.content.startswith('$bye'):
        await message.channel.send("bub-bye!")
    else:
        await message.channel.send("Something is wrong.")

client.run("your token here")

