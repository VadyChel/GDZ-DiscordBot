import discord
from discord.ext import commands


class Errors(commands.Cog):
	def __init__(self, client):
		self.client = client


def setup(client):
	client.add_cog(Errors(client))