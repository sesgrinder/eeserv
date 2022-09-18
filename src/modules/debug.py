# debug.py - Module logging for debug purposes
from discord.ext.commands import Cog, command

class DebugModule(Cog):
	def __init__(self, bot):
		self.server = bot
	
	@command()
	async def debug(self, context, *, text:str):
		await context.send(text)
	
def setup(bot):
	return bot.add_cog(DebugModule(bot))