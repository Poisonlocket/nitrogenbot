import discord
from discord.ext import commands


class Mycogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs are loaded")

    @commands.hybrid_command(name='test2', description='Cogs Slash command test')
    async def test2(self, ctx):
        await ctx.send('Cogs Test running')
async def setup(client):
    await client.add_cog(Mycogs(client))
