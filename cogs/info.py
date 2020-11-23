import datetime
import discord
from discord.ext import commands
from cogs.database import Database 


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

		def get_command_desc(command:commands.command) -> str:
			return " "+command.usage+" ⭐" if command.usage is not None else ""

		for cog in self.client.cogs:
			for command in self.client.get_cog(cog).get_commands():
				emb.add_field(
					name=PREFIX+command.name+get_command_desc(command), 
					value=f"""{"Алиасы: "+", ".join(command.aliases) if command.aliases != [] else ""}\n{command.description}""",
					inline=False
				)

		await ctx.send(embed=emb)

	@commands.command(
		aliases=['моя-история'],
		description="Показывает список ваших запросов"
	)
	async def my_history(self, ctx):
		data = Database().get_logs(ctx.author)
		emb = discord.Embed(title="Ваша история поиска", colour=discord.Color.red())

		for request in data:
			emb.add_field(
				name="Урок: "+request["command_name"], 
				value=f"""Номер задания - {request["number"]}\nВремя - {str(datetime.datetime.fromtimestamp(request["time"]))}""", 
				inline=False
			)

		await ctx.send(embed=emb)

	
	@commands.command(
		aliases=['история'],
		description="Показывает список всех запросов сервера",
		hidden=True
	)
	@commands.has_any_role(761138578331795466, 761138858715774986, 761138258310463539)
	async def history(self, ctx):
		data = Database().get_logs()
		emb = discord.Embed(title="История поиска всех участников", colour=discord.Color.red())

		for request in data:
			emb.add_field(
				name="Участник: "+str(ctx.guild.get_member(
					request["member_id"]
				))+" Урок: "+request["command_name"], 
				value=f"""Номер задания - {request["number"]}\nВремя - {str(datetime.datetime.fromtimestamp(request["time"]))}""", 
				inline=False
			)

		await ctx.send(embed=emb)

def setup(client):
	client.add_cog(Help(client))