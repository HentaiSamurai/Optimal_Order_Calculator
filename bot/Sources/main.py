import sys
import discord
import analysis

client = discord.Client()

# ログインしたとき
@client.event
async def on_ready():
	print('ログインしたわよ')

# だれかが発言したとき
@client.event
async def on_message(message):
	if message.author.bot:
		return
	print(message.author.id, message.content, message.attachments)

	if message.content == '.picture': # 画像受け取りのテスト
		if len(message.attachments) == 0:
			await message.channel.send('画像がないわね...')
		else:
			for attachment in message.attachments:
				img = analysis.imread_web(attachment.url)
			await message.channel.send('受け取ったわよ')
	elif message.content == '.もゆさまおるかー':
		await message.channel.send('いるわよ')
	elif message.content == '.じゃあの':
		await message.channel.send('はいはーい')
		await client.logout()
		await sys.exit()

def get_token():
	with open('../token.txt') as fp:
		token = fp.readline()
	return token

def main():
	token = get_token()
	client.run(token)

if __name__ == "__main__":
    main()