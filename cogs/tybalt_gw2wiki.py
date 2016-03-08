import discord
from discord.ext import commands
from .utils import checks
from __main__ import user_allowed, send_cmd_help
import os

class TybaltWiki:
    """TybaltWiki."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def wiki(search):
        """Search on the Guild Wars 2 wiki
        Example:
        !wiki "Game Updates"
        """
        try:
            await self.bot.say("http://wiki.guildwars2.com/index.php?title=Special%3ASearch&search="+search+"&go=Go")
        except Exception as e:
            print(e)
            await self.bot.say("Something went wrong.")
