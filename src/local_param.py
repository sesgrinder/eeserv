# local_param.py - Resolving specific parameter to its equivalent Python enum
import discord
def get_status(status_str:str)->discord.Status:
	if status_str ==  "online":
		return discord.Status.online
	elif status_str == "offline":
		return discord.Status.offline
	elif status_str == "idle":
		return discord.Status.idle
	elif status_str == "dnd":
		return discord.Status.dnd
	elif status_str == "invisible":
		return discord.Status.invisible

# [FIXME]: Get an activity encode and decode
def get_activity(act_str:str)->discord.BaseActivity:
	return None