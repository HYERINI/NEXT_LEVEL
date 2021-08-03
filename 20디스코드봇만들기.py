import discord 

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.send_message(message.channel, message.content)

client.run('토큰 입력')