using Discord;
using Discord.WebSocket;
using System;
using System.Threading;
using System.Threading.Tasks;

namespace koshoka_bot
{
	public class Program
	{
		private DiscordSocketClient client = default;
		private ISocketMessageChannel currentChannel = default;

		/// <summary>
		/// 初期化
		/// </summary>
		/// <param name="args"></param>
		static void Main(string[] args)
		{
			new Program().MainAsync().GetAwaiter().GetResult();
		}

		/// <summary>
		/// コンストラクタ
		/// </summary>
		public Program()
		{
			client = new DiscordSocketClient();
			client.Log += LogAsync;
			client.Ready += OnReady;
			client.MessageReceived += OnMessage;
		}

		/// <summary>
		/// メインタスク
		/// </summary>
		/// <returns></returns>
		public async Task MainAsync()
		{
			await client.LoginAsync(TokenType.Bot, "");
			await client.StartAsync();

			await Task.Delay(Timeout.Infinite);
		}

		/// <summary>
		/// ログの出力
		/// </summary>
		/// <param name="message"></param>
		/// <returns></returns>
		private Task LogAsync(LogMessage message)
		{
			Console.WriteLine(message.ToString());
			return Task.CompletedTask;                
		}
		
		/// <summary>
		/// 起動したとき
		/// </summary>
		/// <returns></returns>
		private Task OnReady()
		{
			Console.WriteLine("ログインしたわよ");
			return Task.CompletedTask;
		}

		/// <summary>
		/// メッセージを受け取ったとき
		/// </summary>
		/// <param name="message"></param>
		/// <returns></returns>
		private async Task OnMessage(SocketMessage message)
		{
			if (message.Author.IsBot)
				return ;

			Console.WriteLine($"{message.Author.Username}:{message.Content}");

			// 動作チャンネルの設定
			if (message.Content == ".もゆさまおるかー")
			{
				if (currentChannel == null)
				{
					currentChannel = message.Channel;
					await message.Channel.SendMessageAsync("いるわよ");
				}
				else
				{
					await message.Channel.SendMessageAsync($"{currentChannel.Name}にいるわよ");
				}
				return;
			}

			if (currentChannel == null || currentChannel != message.Channel)
			{
				return;
			}

			switch(message.Content)
			{
				case ".じゃあの":
					await message.Channel.SendMessageAsync("はいはーい");
					await client.LogoutAsync();
					Environment.Exit(0);
					break;
				case ".レアスキル":
					await message.Channel.SendMessageAsync("私のレアスキルはこの世の理よ");
					break;
			}
			return;

		}
	}
}
