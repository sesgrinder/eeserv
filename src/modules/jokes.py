# jokes.py - Integrated jokes
from discord.ext.commands import command, Cog

class Jokes(Cog):
	def __init__(self, bot):
		self.server = bot

	@command()
	async def lmao(self, context, *, text:str):
		i = 0
		retstr = ""
		for c in text:
			if i % 2 == 0:
				retstr+=c.lower()
			else:
				retstr+=c.upper()
			i+=1
		await context.send(retstr)

def setup(bot):
	return bot.add_cog(Jokes(bot))