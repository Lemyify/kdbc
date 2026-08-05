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

streaks = {}

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
            
    elif message.content.startswith('/help'):
        await message.channel.send("# commands:\n**/coinflip heads** or **/coinflip tails** - Flip a coin\n**/add 5 7** - Add two numbers\n**/roll 2d6** - Roll dice\n**/bye** - Say goodbye\n**/meme** - Send a random meme\n**/animalmeme** - Send a random animal meme\n**/tip** - Get an eco-friendly tip\n**/challenge** - Complete an eco-friendly challenge\n**/streak** - Check your current streak\n**/complete** - Complete a challenge and update your streak")
        
    elif message.content.startswith('/bye'):
        await message.channel.send("bub-bye!")
        
    elif message.content.startswith('/meme'):
        meme_path = random.choice(['images/mem1.jpeg', 'images/mem2.jpeg', 'images/mem3.jpg', 'images/mem4.jpg', 'images/mem5.jpg'])
        with open(meme_path, 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        
    elif message.content.startswith("/animalmeme"):
        animal_path = random.choice(['animals/animal1.jpg', 'animals/animal2.jpg', 'animals/animal3.jpg', 'animals/animal4.jpg', 'animals/animal5.jpg', 'animals/animal6.jpg', 'animals/animal7.jpg'])
        with open(animal_path, 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    
    elif message.content.startswith("/tip"):
        tips = [
            " use a reusable water bottle instead of buying plastic bottles.",
            " Bring a reusable shopping bag when you go shopping.",
            " Recycle paper, plastic, glass, and metal whenever possible.",
            " turn off lights when you leave a room to save energy.",
            " Take shorter showers to save water.",
            " Avoid wasting food by only taking what you'll eat.",
            " Use a reusable cup instead of disposable ones.",
            " Print only when necessary to save paper.",
            " Walk or cycle instead of driving short distances.",
            " Say no to plastic straws when you don't need one."
        ]

        tip = random.choice(tips)
        await message.channel.send("🌿 **Eco Tip:** " + tip)
    
    elif message.content.startswith("/challenge"):
        challenges = [
            " Use a reusable water bottle for the whole day.",
            " bring a reusable shopping bag on your next shopping trip.",
            " Take a 5-minute shower today.",
            " Turn off all lights when you leave a room.",
            " Avoid using any single-use plastic today.",
            " wwalk or cycle instead of using a car for a short journey.",
            " Finish all the food on your plate to avoid waste.",
            " use both sides of a sheet of paper before recycling it.",
            " Recycle at least five items today.",
            " Pick up three pieces of litter if it's safe to do so."
        ]

        challenge = random.choice(challenges)
        await message.channel.send("🌍 **Today's Eco Challenge:** " + challenge)
    
    elif message.content.startswith("/streak"):
        user_id = message.author.id

        if user_id not in streaks:
            streaks[user_id] = 0

        await message.channel.send(
            "🔥 " + message.author.mention + ", your current streak is ** " + str(streaks[user_id]) + " ** days!"
        )
    
    elif message.content.startswith("/complete"):
        user_id = message.author.id

        if user_id not in streaks:
            streaks[user_id] = 0

        streaks[user_id] += 1

        await message.channel.send(
            "🎉 Challenge completed! Your streak is now ** " + str(streaks[user_id]) + " ** days! 🔥"
        )
    
    elif message.content.startswith("/recycle"):
        item = message.content.replace("/recycle ", "").lower()

        recycling = {
            "plastic bottle": " rinse it out and put it in the recycling bin.",
            "glass bottle": " Put it in the glass recycling bin.",
            "paper": " Clean paper can be recycled.",
            "cardboard": " flatten it before recycling.",
            "battery": " Don't put it in your recycling bin. Use a battery recycling point."
        }

        if item in recycling:
            await message.channel.send(recycling[item])
        else:
            await message.channel.send(
                "🤔 I don't know how to recycle **" + item + "**."
            )
    
    else:
        await message.channel.send("didn't understand that command.")

client.run("YOUR_BOT_TOKEN_HERE")

