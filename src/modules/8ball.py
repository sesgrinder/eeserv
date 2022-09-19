# 8ball.py - 8 ball module
# Just to test UI system so this probably do not get merge in to main
# So I just reign free here

from discord.ext.commands import command, Cog
import discord

class ChooseButton(discord.ui.Button):
	def __init__(self, text, parent):
		super().__init__(label=text)
		self.text = text
		self.parent = parent
	
	async def callback(self, interact):
		await interact.channel.send(f"{self.text} choosen.")
		self.parent.stop()

class Choice(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.buttons = []
	
	def init_button(self, texts:tuple):
		for text in texts:
			but = ChooseButton(text, self)
			self.add_item(but)
	
		

class Balls(Cog):
	def __init__(self, bot):
		self.server = bot
	
	@command()
	async def ball(self,context, *text):
		if len(text) < 2 :
			await context.send("Command Invalid.\nUsage: `?ball <choice 1> <choice 2`")
			return
		
		uic = Choice()
		uic.init_button(text)

		await context.send("Choosing ...", view=uic)

		await uic.wait()




def setup(bot):
	return bot.add_cog(Balls(bot))