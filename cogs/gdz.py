import discord
import pymongo
from discord.ext import commands

class GDZ(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(
		aliases=["алгебра"],
		description="Отправляет гдз по номеру из алгебры",
		usage="[Номер задания]"
	)
	async def algebra(self, ctx, number):
		pass

	@commands.command(
		aliases=["геометрия", "геометрія"],
		description="Отправляет гдз по номеру из геометрии",
		usage="[Номер задания]"
	)
	async def geometry(self, ctx, number):
		pass

	@commands.command(
		aliases=["укр-язык", "укр-мова"],
		description="Отправляет гдз по номеру из украинского языка",
		usage="[Номер задания]"	
	)
	async def ukr_language(self, ctx, number):
		pass

def setup(client):
	client.add_cog(GDZ(client))