import discord
from discord.ext import commands


class Errors(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.errors.CommandNotFound):
			pass
		elif isinstance(error, commands.errors.MissingRequiredArgument):
			await ctx.send(
				embed=discord.Embed(
					title="Ошибка!",
					description="Укажите номер задания!",
					colour=discord.Color.red()
				)
			)
		else:
			raise error

def setup(client):
	client.add_cog(Errors(client))