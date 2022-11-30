import discord
from flask import Flask
app = Flask(__name__)


TOKEN = 'MTA0MDY0NjUzNDIwMDU3Mzk3Mg.GBlogr.zimYLe1gPMuh4_PsJEPirfS3AkqoLBGTcgAcEg'

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
