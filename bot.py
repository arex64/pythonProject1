import discord
from discord.ext import commands
from discord.ext.commands import check
from Controller import BotController

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)  # dastoori ke bahash bot o farakhani mikonim


@client.event
async def on_ready():  # message i ke bot vaghti shooroo mishe neshoon mide
    print('Bot is ready')


@client.command()
async def mute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)
        print('Muted')


@client.command()
async def message_history(cxt):
    message = BotController.retrieve_messages('1117719750781448275')
    await cxt.reply("" + str(message) + "")

@client.command()
async def unmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)
        print('Unmute')
    await ctx.send('All users are Unmute')


# check to make sure ctx.author.voice.channel exists
def invoice_channel():
    def predicate(ctx):
        return ctx.author.voice and ctx.author.voice.channel

    return check(predicate)


@invoice_channel()
# moving users to another channel

@client.command()
async def move(ctx, *, channel: discord.VoiceChannel):
    for members in ctx.author.voice.channel.members:
        await members.move_to(channel)
        await ctx.send("Users moved to" + ' ' + str(channel))


@client.command()
async def dm(ctx, *, args=None):
    if args != None:
        members = ctx.author.voice.channel.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' send to: " + member.name)

            except:
                print("Couldn't send '" + args + "' to" + member.name)
    else:
        await ctx.channel.send(" No provided Argument")

client.run('MTExNzM5MDc4NjQzOTQyMTk1Mg.G1Cwtk.-8MVoiSCT45nlSdXkRh7K3NKOYNyCSaaezkzy8')  # run shodan bot
