import discord
from flask import Flask
app = Flask(__name__)


TOKEN = 'MTA0NDI0Mjc1NTQ5NDM1NDk4Ng.GmdmOt.dGuvst2LK00EcmVjZGOmmaeE9PNosbYckDK8W4'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('Send')
client.run(TOKEN)

@app.route('/')
def hello_world():
    return 'Hello, World!'
