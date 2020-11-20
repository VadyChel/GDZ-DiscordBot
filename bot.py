import os
import discord
from colorama import *
from discord.ext import commands

init()

client = commands.Bot(
	command_prefix=".",
	case_insensitive=True, 
	intents=discord.Intents.all()
)
client.remove_command("help")

@client.event
async def on_ready():
	print(
		Fore.MAGENTA
		+ f"[GDZ-SYSTEM-LOGGING]:::{client.user.name} is connected to discord server"
		+ Fore.RESET
	)
	await client.change_presence(
		status=discord.Status.dnd, activity=discord.Game(" .help ")
	)

@client.command()
@commands.is_owner()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	print(Fore.GREEN + f"[GDZ-SYSTEM-COG]:::{extension.upper()} - Loaded")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	print(Fore.GREEN + f"[GDZ-SYSTEM-COG]:::{extension.upper()} - Unloaded")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	client.load_extension(f"cogs.{extension}")
	print(Fore.GREEN + f"[GDZ-SYSTEM-COG]:::{extension.upper()} - Reloaded")

@client.command()
@commands.is_owner()
async def ping(ctx):
	await ctx.send(str(round(client.latency*1000)))

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")
		print(Fore.GREEN + f"[GDZ-SYSTEM-COG]:::{filename[:-3].upper()} - Loaded")

print(Fore.RESET)
client.run(os.environ["BOT_TOKEN"])