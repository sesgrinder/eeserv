import os
import sys
import json
from discord.ext.commands import Cog
import utils

API_URL_NHENTAI = "https://nhentai.net/api/gallerry/"
LINK_URL_NHENTAI = "https://nhentai.net/g/"

class Nhentai(Cog):
	def __init__():
		pass

	def get_JSON(number):
		gallery_number = str(number)
		# [FIXME]: Request cached database
		gallery_link = f"{API_URL_NHENTAI}{gallery_number}"
		res = utils.get_wrapper(gallery_link)
		if res.status_code == 200:
			data = res.text
			api_data = json.load(data)
			
			# Unfinished due to no way to test (Nhentai turn on cloudflare even for its dedicated API page)
			# In the mean time do not touch this as it is not compatible with others cog