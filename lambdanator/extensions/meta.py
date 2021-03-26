from discord.ext import commands


class Meta(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """
        Sends the bot's websocket latency
        """
        await ctx.send(
            f"\N{TABLE TENNIS PADDLE AND BALL} {round(ctx.bot.latency * 1000)}ms"
        )

def setup(bot):
    bot.add_cog(Meta(bot))
