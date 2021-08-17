import discord
import os
import pandas as pd

client = discord.Client()

quotes = pd.read_csv('wisdom.csv')

morning_variations = ["Good Morning", "good morning", "Good morning", "Morning", "morning"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return None

  if message.content.startswith('$wisdom'):
    quote = quotes.sample(1) #Gets a random Quote
    await message.channel.send("Here are some words of wisdom by " + quote.loc[:,'authors'].reset_index(drop=True)[0] + " for you!\n" + '"' +quote.loc[:,'quotes'].reset_index(drop=True)[0] + '"')

  if any(word in message.content for word in morning_variations):
    quote = quotes.sample(1) 
    await message.channel.send("Good morning! Here are words of wisdom from " + quote.loc[:,'authors'].reset_index(drop=True)[0] + " to start the day off right!\n" + '"' + quote.loc[:,'quotes'].reset_index(drop=True)[0] + '"')

client.run(
os.environ['TOKEN']
)