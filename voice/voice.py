import discord
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
        gmember: discord.Member = self.bot.get_guild(self.bot.guild_id).get_member(thread.recipient.id)
        if gmember and gmember.voice:
            embed = discord.Embed(
            description=f'This User is currently in Voice Channel {gmember.voice.channel.mention}.',
            color=discord.Color.blue()
            )
            await thread.channel.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Voice(bot))