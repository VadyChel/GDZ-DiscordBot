import os
import time
import discord
from pymongo import MongoClient

class Database:
	def __init__(self):
		self._dbname = os.environ.get("DATABASE_NAME")
		self._dbpass = os.environ.get("DATABASE_PASS")
		self.cluster = MongoClient(
			f"mongodb+srv://vadym:{self._dbpass}@gdz-botdb.5lufl.mongodb.net/{self._dbname}?retryWrites=true&w=majority"
		)
		self.database = self.cluster["gdzData"]
		self.collection = self.database["logs"]

	def set_log(
		self, 
		member:discord.Member, 
		num:int, 
		name:str
	) -> None:
		self.collection.insert_one({
			"_id": self.collection.count(),
			"member_id": member.id,
			"number": num,
			"command_name": name,
			"time": time.time()
		})

	def get_logs(self, member:discord.Member=None) -> list:
		if member is not None:
			return self.collection.find({
				"member_id": member.id
			})
		else:
			return self.collection.find()