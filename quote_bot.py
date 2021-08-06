import discord
import os
import pandas as pd

client = discord.Client()

quotes = pd.read_csv('Web_scraping/motivation.csv')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return None

  if message.content.startswith('$motivate'):
    quote = quotes.sample(1) #Gets a random Quote
    await message.channel.send("Here is a little quote to motivate you!\n" + quote.loc[:,'quotes'].reset_index(drop=True)[0] + " - " + quote.loc[:,'authors'].reset_index(drop=True)[0])

  if message.content.startswith('$options'):
    await message.channel.send("$motivate")

client.run(
os.environ['TOKEN']
)