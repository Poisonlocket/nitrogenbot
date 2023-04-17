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

    # Embed Command to change color to users color color = ctx.author.color
    @commands.hybrid_command(name='embed', description='embed command')
    async def embed(self, ctx):
        embed_message = discord.Embed(title='Embed Title', description='Description of Embed',
                                      color=discord.Color.blue())

        embed_message.set_author(name=f'Requested by {ctx.author.mention}', icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name='Field Name', value='Field Value', inline=False)
        embed_message.set_footer(text='This is the footer', icon_url=ctx.author.avatar)

        await ctx.send(embed=embed_message)


async def setup(client):
    await client.add_cog(Mycogs(client))
