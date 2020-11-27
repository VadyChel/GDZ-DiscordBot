import json
import requests
import discord
import pymongo
from bs4 import BeautifulSoup as bs
from discord.ext import commands


class GDZ(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.algebra_base_url = "https://vshkole.com/8-klass/reshebniki/algebra/ag-merzlyak-vb-polonskij-ms-yakir-2016/"
		self.algebra_numbers = {
			json.dumps(list(range(1, 27))): "1-ratsionalni-virazi/1-ratsionalni-drobi/",
			json.dumps(
				list(range(27, 68))
			): "1-ratsionalni-virazi/2-osnovna-vlastivist-ratsionalnogo-drobu/",
			json.dumps(
				list(range(68, 98))
			): "1-ratsionalni-virazi/3-dodavannya-i-vidnimannya-ratsionalnih-drobiv-z-odnakovimi-znamennikami/",
			json.dumps(
				list(range(98, 143))
			): "1-ratsionalni-virazi/4-dodavannya-i-vidnimannya-ratsionalnih-drobiv-z-riznimi-znamennikami/",
			json.dumps(
				list(range(143, 176))
			): "1-ratsionalni-virazi/5-mnozhennya-i-dilennya-ratsionalnih-drobiv-pidnesennya-ratsionalnogo-drobu-do-stepenya/",
			json.dumps(
				list(range(176, 205))
			): "1-ratsionalni-virazi/6-totozhni-peretvorennya-ratsionalnih-viraziv/",
			json.dumps(
				list(range(205, 231))
			): "1-ratsionalni-virazi/7-rivnosilni-rivnyannya-ratsionalni-rivnyannya/",
			json.dumps(
				list(range(231, 274))
			): "1-ratsionalni-virazi/8-stepin-iz-tsilim-vidyemnim-pokaznikom/",
			json.dumps(
				list(range(274, 312))
			): "1-ratsionalni-virazi/9-vlastivosti-stepenya-iz-tsilim-pokaznikom/",
			json.dumps(
				list(range(312, 350))
			): "1-ratsionalni-virazi/10-funktsiya-ta-yiyi-grafik/",
			json.dumps(
				list(range(350, 377))
			): "2-kvadratni-koreni-dijsni-chisla/11-funktsiya-u-h2-ta-yiyi-grafik/",
			json.dumps(
				list(range(377, 422))
			): "2-kvadratni-koreni-dijsni-chisla/12-kvadratni-koreni-arifmetichnij-kvadratnij-korin/",
			json.dumps(
				list(range(422, 443))
			): "2-kvadratni-koreni-dijsni-chisla/13-mnozhina-ta-yiyi-elementi-pidmnozhina/",
			json.dumps(
				list(range(443, 471))
			): "2-kvadratni-koreni-dijsni-chisla/14-chislovi-mnozhini/",
			json.dumps(
				list(range(471, 499))
			): "2-kvadratni-koreni-dijsni-chisla/15-vlastivosti-arifmetichnogo-kvadratnogo-korenya/",
			json.dumps(
				list(range(499, 556))
			): "2-kvadratni-koreni-dijsni-chisla/16-totozhni-peretvorennya-viraziv-yaki-mistyat-kvadratni-koreni/",
			json.dumps(
				list(range(556, 591))
			): "2-kvadratni-koreni-dijsni-chisla/17-funktsiya-ta-yiyi-grafik/",
			json.dumps(
				list(range(591, 631))
			): "3-kvadratni-rivnyannya/18-kvadratni-rivnyannya-rozvyazuvannya-nepovnih-kvadratnih-rivnyan/",
			json.dumps(
				list(range(631, 679))
			): "3-kvadratni-rivnyannya/19-formula-koreniv-kvadratnogo-rivnyannya/",
			json.dumps(
				list(range(680, 726))
			): "3-kvadratni-rivnyannya/20-teorema-viyeta/",
			json.dumps(
				list(range(726, 750))
			): "3-kvadratni-rivnyannya/21-kvadratnij-trichlen/",
			json.dumps(
				list(range(750, 777))
			): "3-kvadratni-rivnyannya/22-rozvyazuvannya-rivnyan-yaki-zvodyatsya-do-kvadratnih-rivnyan/",
			json.dumps(
				list(range(777, 814))
			): "3-kvadratni-rivnyannya/23-ratsionalni-rivnyannya-yak-matematichni-modeli-realnih-situatsij/",
		}

	@commands.command(
		aliases=["алгебра"],
		description="Отправляет гдз по номеру из алгебры",
		usage="[Номер задания]",
	)
	async def algebra(self, ctx, number: int):
		if number < 1 or number > 813:
			await ctx.send(
				embed=discord.Embed(
					title="Ошибка!",
					description="Указан номер задания в не правильном диапазоне! Укажите от 1 до 813",
					colour=discord.Color.red(),
				)
			)

		for key, value in self.algebra_numbers.items():
			if number in json.loads(key):
				url_group = value
				break

		url = self.algebra_base_url + url_group + str(number)
		headers = {
			"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
		}
		html = requests.get(url, headers=headers).text
		soup = bs(html, "lxml")
		url_img = (
			soup.find("div", {"class": "img-content"})
			.find("p")
			.find("img")
			.attrs["src"]
		)
		emb = discord.Embed(
			title=f"Ответ к {number} заданию", colour=discord.Color.red()
		)
		emb.set_image(url=url_img)
		await ctx.send(embed=emb)

	@commands.command(
		aliases=["геометрия", "геометрія"],
		description="Отправляет гдз по номеру из геометрии",
		usage="[Номер задания]",
	)
	async def geometry(self, ctx, number):
		print("g")

	@commands.command(
		aliases=["укр-язык", "укр-мова"],
		description="Отправляет гдз по номеру из украинского языка",
		usage="[Номер задания]",
	)
	async def ukr_language(self, ctx, number):
		pass


def setup(client):
	client.add_cog(GDZ(client))
