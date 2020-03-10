from discord.ext.commands import Cog

from journey import Journeybot


class BaseCog(Cog):
    def __init__(self, bot):
        self.bot: Journeybot = bot
