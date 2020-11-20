import discord
from discord.ext import commands


class Help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["хелп"])
	async def help(self, ctx):
		emb = discord.Embed(title="Доступные команды", colour=discord.Color.red())
		for command in self.client.get_commands():
			emb.add_field(name=self.client.get_prefix()+command.name, value=command.description)

		await ctx.send(embed=emb)

def setup(client):
	client.add_cog(Help(client))