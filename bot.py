import os
import discord
from colorama import *
from cogs.database import Database
from discord.ext import commands

init()

client = commands.Bot(
	command_prefix=".", case_insensitive=True, intents=discord.Intents.all()
)
client.remove_command("help")

extensions = ("errors", "gdz", "info")


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


@client.event
async def on_command(ctx):
	if ctx.command is not None and ctx.command.name in [
		alias for c in client.get_cog("GDZ").get_commands() for alias in c.aliases
	] + [c.name for c in client.get_cog("GDZ").get_commands()] and ctx.args[2] is not None:
		Database().set_log(
			member=ctx.author, num=int(ctx.args[2]), name=ctx.command.name
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
	await ctx.send(str(round(client.latency * 1000)))


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		if filename[:-3] in extensions:
			client.load_extension(f"cogs.{filename[:-3]}")
			print(Fore.GREEN + f"[GDZ-SYSTEM-COG]:::{filename[:-3].upper()} - Loaded")

print(Fore.RESET)
client.run(os.environ["BOT_TOKEN"])
