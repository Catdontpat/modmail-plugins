from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
        msg = thread.genesis_message
        try:
            channel = creator.voice.channel
            if channel:
                embed = discord.Embed(
                    description=f'<@{creator.id}> is currently in <#{channel.id}>')
                thread.send(embed=embed)
            else:
                return
        except AttributeError:
            return await thread.send('An error has occurred.')
        
async def setup(bot):
    await bot.add_cog(Voice(bot))