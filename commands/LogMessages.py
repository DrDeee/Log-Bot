import discord
from datetime import datetime
from discord import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command


class Log(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
			self.log_channel = self.bot.get_channel(870282114510233690)
			self.bot.cogs_ready.ready_up("log")

	@Cog.listener()
	async def on_message_edit(self, before, after):
		#if not after.author.bot:
			if before.content != after.content:
				embed = Embed(

					title="Message edited",
					description=f"A [message]({after.jump_url}) from {after.author.mention} ({after.author.id}) in {after.channel.mention} was edited",
					colour = discord.Colour.orange(),
					timestamp=datetime.utcnow()
				)
				embed.set_footer(text=f"Message ID: {after.id}")

				fields = [("Before", before.content, False),
						  ("After", after.content, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)

				await self.log_channel.send(embed=embed)

	@Cog.listener()
	async def on_message_delete(self, message):
		#if not message.author.bot:
			embed = Embed(

                title=f"{message.author.avatar.url} Message deleted",
				description=f"A message from {message.author.mention} ({message.author.id}) in {message.channel.mention} was deleted",
				colour = discord.Colour.red(),
				timestamp=datetime.utcnow()
            )
			embed.set_footer(text=f"Message ID: {message.id}")
			fields = [("Content", message.content, False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed=embed)

def setup(bot):
	bot.add_cog(Log(bot))