import discord
from discord.ext import commands, tasks
import asyncio

# Set up the bot with necessary intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Global variable to store the target channel
target_channel_id = 1318961284955377664

@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user}")

# Command to set the target channel
@bot.command(name="setchannel")
async def set_channel(ctx, channel_id: int):
    global target_channel_id
    target_channel_id = 1318961284955377664
    await ctx.send(f"Target channel set to <#{channel_id}>.")

# Command to start spamming the target channel
@bot.command(name="startspam")
async def start_spam(ctx):
    if target_channel_id is None:
        await ctx.send("Target channel is not set. Use `!setchannel <channel_id>` first.")
        return

    channel = bot.get_channel(target_channel_id)
    if channel is None:
        await ctx.send("Invalid channel ID. Make sure the bot has access to the channel.")
        return

    await ctx.send(f"Starting educational spam in <#{target_channel_id}>.")
    for i in range(10):  # Send 10 messages as an example
        await channel.send(f"This is educational spam message {i + 1}.")
        await asyncio.sleep(2)  # Wait 2 seconds between messages

    await ctx.send("Educational spam completed.")

# Command to stop the bot
@bot.command(name="stop")
async def stop(ctx):
    await ctx.send("Bot is shutting down. Goodbye!")
    await bot.close()

# Run the bot with your token
bot.run("user_token")
