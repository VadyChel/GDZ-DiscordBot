import discord
from discord.ext import commands


class Help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(
		aliases=["хелп"],
		description="Показывает список доступных команд"
	)
	async def help(self, ctx):
		PREFIX = await self.client.get_prefix(ctx.message)
		emb = discord.Embed(title="Доступные команды", colour=discord.Color.red())
		for cog in self.client.cogs:
			for command in self.client.get_cog(cog).get_commands():
				emb.add_field(
					name=f"{PREFIX+command.name} {command.usage if command.usage is not None else ""}", 
					value=f"""{"Алиасы: "+", ".join(command.aliases) if command.aliases != [] else ""}\n{command.description}""",
					inline=False
				)

		await ctx.send(embed=emb)

def setup(client):
	client.add_cog(Help(client))