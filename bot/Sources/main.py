import sys
import discord
import analysis
import sheet
import command

client = discord.Client()

# botが稼働しているチャンネル
current_channel = None

# ログインしたとき
@client.event
async def on_ready():
	print('ログインしたわよ')

# だれかが発言したとき
@client.event
async def on_message(message):
	global current_channel

	if message.author.bot:
		return
	print(message.author.id, message.content, message.attachments)

	if message.content == '.もゆさまおるかー':
		current_channel = message.channel
		print(current_channel.name, 'にいるわ')
		await current_channel.send('いるわよ')

	# もゆさまは呼ばないと出てきてくれない
	# 別のチャンネルでは反応しない
	if current_channel is None or current_channel != message.channel:
		return
	
	elif message.content == '.picture': # 画像受け取りのテスト
		if len(message.attachments) == 0:
			await current_channel.send('画像がないわね...')
		else:
			for attachment in message.attachments:
				img = analysis.imread_web(attachment.url)
			await current_channel.send('受け取ったわよ')
	elif message.content == '.じゃあの':
		await current_channel.send('はいはーい')
		await client.logout()
		await sys.exit()
	elif message.content == '.add player':
		user = message.author
		command.add_player(user.id, user.display_name)
		await current_channel.send("{} を登録したわ".format(user.display_name))
	elif message.content == '.remove player':
		user = message.author
		if command.remove_player(user.id, user.display_name):
			await current_channel.send("{} を削除したわ".format(user.display_name))
		else:
			await current_channel.send("{} は登録されてないわね".format(user.display_name))

def get_token():
	with open('../token.txt') as fp:
		token = fp.readline()
	return token

def main():
	token = get_token()
	client.run(token)

if __name__ == "__main__":
    main()