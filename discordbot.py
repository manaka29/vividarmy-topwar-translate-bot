from discord.ext import commands
import os
import traceback
import json
import unicodedata

bot = commands.Bot(command_prefix='$')
token = os.environ['DISCORD_BOT_TOKEN']

vividarmy_file = open('./data/vividarmy.json','r')
vividarmy_dict = json.load(vividarmy_file)
topwar_file = open('./data/topwar.json', 'r')
topwar_dict = open(topwar_file)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name="vividarmy")
async def _vividarmy(ctx, *args):
    response = ''
    for arg in args:
        normalized = unicodedata.normalize('NKFC', arg)
        if normalized not in vividarmy_dict:
            response += '{} : NOT DEFINED\n'.format(normalized)
        else:
            response += '{} : {}\n'.format(normalized, vividarmy_dict[normalized])
    await ctx.send(response.rstrip('\n'))


bot.run(token)
