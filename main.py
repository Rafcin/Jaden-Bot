import discord
from discord.ext import commands
import gpt_2_simple as gpt2

model_name = "774M"
run_name = 'run1'

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name=model_name)

TOKEN = 'NjIxODg4ODg3ODI3OTg4NTAx.XXyKrw.4wBCYunzuKxz8UuXpZeu7KCEvb8'
description = 'Use the prefix . to summon the Jaden.'
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    """-Tonto says hello!"""
    await ctx.send('Hello! I am Jaden Bot, a clone of my original host Jaden. I was designed to act as the Jaden replacment in the event people can not locate or access their local Jaden.')

@bot.command()
async def story(ctx,*,input):
    """-Makes Jaden tell a story."""
    await ctx.send("")
    result = gpt2.generate(
        sess, 
        model_name=model_name,
        top_k=40, 
        top_p = 0.9,
        prefix=input, 
        truncate='<|endoftext|>', 
        length=100, 
        temperature=0.7,
        nsamples=1,
        batch_size=1,
        return_as_list=True
        )[0]
    await ctx.send(result)


@bot.command()
async def say(ctx, input: str):
    """-Tonto will repeate what you write."""
    await ctx.send(input.split(" "))

@bot.command()
async def cmds(ctx):
    """-Will list commands if you can't use .help."""
    with open('help.txt', 'r') as hfile:
        data = hfile.read()
    await ctx.send(data)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run(TOKEN)