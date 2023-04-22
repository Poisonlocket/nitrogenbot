import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
from dotenv import load_dotenv
from os import getenv
import os
import asyncio

load_dotenv("token.env")
my_token = getenv("TOKEN")
my_token = str(my_token)

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot_status = cycle(['Bubbling', 'steaming', 'Cooling'])


# loading cogs
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start(my_token)


# changing status
@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


# terminal message to check if bot has started
@client.event
async def on_ready():
    try:
        await client.tree.sync()
        print("Nitrogen is now Bubbling")
    except Exception as error:
        print(error)
    change_status.start()


@client.hybrid_command(name='test', description='Test command')
async def test(ctx):
    await ctx.send('Test')


# magic eightball command with answer txt file linked
@client.command(aliases=['8ball'])
async def magic_eightball(ctx):
    with open("C:\\Users\\lorib\\PycharmProjects\\Nitrogenbot\\answers.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
        await ctx.send(response)


@client.hybrid_command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, modreason):
    await ctx.guild.kick(member)

    conf_embed = discord.Embed(title='Success!', colour=discord.Color.green())
    conf_embed.add_field(name='Kicked:',
                         value=f'{member.mention} has been kicked from the server by {ctx.author.mention}.',
                         inline=False)
    conf_embed.add_field(name='Reason:', value=modreason, inline=False)

    await ctx.send(embed=conf_embed)


asyncio.run(main())
