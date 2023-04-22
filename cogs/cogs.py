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

    # Moderation commands
    # message clear command with x amount of messages
    @commands.hybrid_command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f'{count} messages have been deleted')

    @commands.hybrid_command(name='Kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.kick(member)

        conf_embed = discord.Embed(title='Success!', colour=discord.Color.green())
        conf_embed.add_field(name='Kicked:',
                             value=f'{member.mention} has been kicked from the server by {ctx.author.mention}.',
                             inline=False)
        conf_embed.add_field(name='Reason:', value=modreason, inline=False)

        await ctx.send(embed=conf_embed)

    @commands.hybrid_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, modreason):
        await ctx.guild.ban(member)

        ban_conf_embed = discord.Embed(title='Success!', colour=discord.Color.green())
        ban_conf_embed.add_field(name='Kicked:',
                                 value=f'{member.mention} has been banned from the server by {ctx.author.mention}.',
                                 inline=False)
        ban_conf_embed.add_field(name='Reason:', value=modreason, inline=False)

        await ctx.send(embed=ban_conf_embed)

    @commands.hybrid_command(name='unban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userid):
        user = discord.Object(id=userid)
        await ctx.guild.unban(user)

        conf_embed = discord.Embed(title='Success!', colour=discord.Color.green())
        conf_embed.add_field(name='Unbanned:',
                             value=f'<@{userid}> has been unbanned from the server by {ctx.author.mention}.',
                             inline=False)

        await ctx.send(embed=conf_embed)


async def setup(client):
    await client.add_cog(Mycogs(client))
