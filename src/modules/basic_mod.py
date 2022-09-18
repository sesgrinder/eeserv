# basic_mod.py - Basic moderation tool
from discord.ext.commands import command, Cog
class BasicMod(Cog):
	def __init__(self, bot):
		self.server = bot

def setup(bot):
	return bot.add_cog(BasicMod(bot))