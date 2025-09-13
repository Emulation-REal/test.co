import discord
from discord.ext import commands
import asyncio

# Set up the bot with required intents
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Send DMs to all friends or open DM channels
@bot.command()
async def spam(ctx, *, message):
    # Check if the command is run by the bot owner to prevent misuse
    if ctx.author.id != 1203184708566130749:  # Replace with your Discord user ID
        await ctx.send("You are not authorized to use this command.")
        return

    sent_count = 0
    failed_count = 0

    # Iterate through all open DM channels
    for dm_channel in bot.private_channels:
        try:
            await dm_channel.send(message)
            print(f"Sent message to {dm_channel.recipient.name}")
            sent_count += 1
            # Add a delay to avoid rate limiting
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Failed to send message to {dm_channel.recipient.name}: {e}")
            failed_count += 1

    # Optionally, send to friends (requires user token or specific permissions)
    # Note: Accessing friends list typically requires a user token, which is against Discord's ToS for bots
    # This part is commented out to comply with Discord's guidelines
    """
    for friend in bot.user.friends:  # This requires a user client, not a bot client
        try:
            await friend.send(message)
            print(f"Sent message to {friend.name}")
            sent_count += 1
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Failed to send message to {friend.name}: {e}")
            failed_count += 1
    """

    await ctx.send(f"Finished sending messages. Sent: {sent_count}, Failed: {failed_count}")

# Replace with your bot token
bot.run('YOUR_BOT_TOKEN')
