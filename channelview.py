import discord
from discord.ext import commands

from datetime import datetime

from core import checks
from core.models import PermissionLevel

class ModmailView(commands.Cog): 
    """Commands to give members access to text channels."""
    
    def __init__(self, bot):
        self.bot = bot

	@commands.command()
	@checks.has_permissions(PermissionLevel.ADMIN)
	async def addview(self,
					  ctx: commands.Context,
					  user: discord.Member = None,
					  channel: discord.TextChannel = None):
		"""
  		Give a member access to view the channel.
  		The correct syntax is "{prefix}addview [user] [channel]"
  		"""
		if user:
			if not channel:
				channel = ctx.channel
			
			channel.edit(
				overwrites = {
					user: discord.PermissionOverwrite(read_messages = True)
				}
			)

			await ctx.send(embed = discord.Embed(
						name = "Success!",
						description = f"{user.mention} has been added to the channel!",
						color = 0x11db02,
						timestamp = datetime.now()
					))
		else:
			await ctx.send(embed = discord.Embed(
						name = "Wrong Syntax!",
						description = "Correct Usage:```\naddview [user] [channel]\n```",
						color = 0xbf0000,
						timestamp = datetime.now()
					))

	@commands.command()
	@checks.has_permissions(PermissionLevel.ADMIN)
	async def removeview(self,
					  ctx: commands.Context,
					  user: discord.Member = None,
					  channel: discord.TextChannel = None):
		"""
  		Remove the access for a member to view the channel.
  		The correct syntax is "{prefix}removeview [user] [channel]"
  		"""
		if user:
			if not channel:
				channel = ctx.channel
			
			channel.edit(
				overwrites = {
					user: discord.PermissionOverwrite(read_messages = True)
				}
			)

			await ctx.send(embed = discord.Embed(
						name = "Success!",
						description = f"{user.mention} has been removed from the channel!",
						color = 0x11db02,
						timestamp = datetime.now()
					))
			
		else:
			await ctx.send(embed = discord.Embed(
						name = "Wrong Syntax!",
						description = "Correct Usage:```\nremoveview [user] [channel]\n```",
						color = 0xbf0000,
						timestamp = datetime.now()
					))
			
def setup(bot):
    bot.add_cog(ModmailView(bot))