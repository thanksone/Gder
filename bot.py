import discord
T = open("token.txt", 'r').read();
ints = discord.Intents.all();
bot = discord.Client(intents = ints);
channel_id = [1270768936966684772, 1270766989312266311, 1270781417797976146, 1270781783096557608, 1270782049053315132, 1270783094890172538, 1270783334620074056, 1270785759707791472, 1270786026755067997, 1270786823400063076, 1270821913287065713];
call_cnt = [];
max_cnt = [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2];
closecard = {"信徒的話" : 3, "藍菈娜的故事" : 5, "獻祭儀式" : 6, "廢棄倉庫的冤魂" : 10};
can = ["並沒有", "不要瞎掰好嗎", "這顯然是廠商的疏失"];
def ran_can():
	return 
@bot.event
async def on_ready():
	for i in range(0, 11):
		call_cnt.append([]);
		for j in range(0, 12):
			call_cnt[i].append(0);
	print("logged in as", end = ' ');
	print(bot.user);
@bot.event
async def on_message(msg : discord.Message):
	if msg.author == bot.user:
		return;
	try:
		if msg.channel.id == channel_id[0]:
			update = msg.content.split();
			for i in range(0, len(update)):
				update[i] = int(update[i]);
			if call_cnt[update[0]][update[1]] == 0:
				call_cnt[update[0]][update[1]] = 1;
				grp = update[0];
				cls = update[1];
			else:
				await msg.channel.send(can[0]);
				return;
		else:
			cc = closecard[msg.content];
			for i in range(1, 11):
				if msg.channel.id == channel_id[i]:
					if call_cnt[i][cc] == 1 and max_cnt[cc] == 2:
						call_cnt[i][cc] = 2;
						grp = i;
						cls = cc;
					else:
						await msg.channel.send(can[0]);
						return;
		if call_cnt[grp][cls] == max_cnt[cls]:
			put_channel = bot.get_channel(channel_id[grp]);
			if cls == 0:
				await put_channel.send(file = discord.File("map/map_0.jpg"));
				with open("people/yourself.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("people/another_me.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("people/aranara.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/pre.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			elif cls == 1:
				with open("people/police.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("people/police.png"));
				with open("linelock/star.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/N.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/police_guess.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			elif cls == 2:
				with open("people/villager.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("people/villager.png"));
				with open("linelock/shake_salt.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			elif cls == 3:
				with open("people/desciple.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("people/desciple.jpg"));
				with open("linelock/server.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/AC.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("linelock/genshin.png"));
			elif cls == 4:
				with open("people/ghost.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("people/ghost.jpg"));
				with open("linelock/dead_body.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/AC.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("linelock/dead_body.jpg"));
			elif cls == 5:
				with open("linelock/turtle_soup.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/love.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			elif cls == 6:
				with open("people/Gsus.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/sacrafice.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/loli.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			elif cls == 7:
				with open("people/imoto.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/dairy.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/bunny.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("linelock/bunny.jpg"));
			elif cls == 8:
				with open("people/lorenzo.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/wierd_aranara.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/de_aranara.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			elif cls == 9:
				with open("people/doctor.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				await put_channel.send(file = discord.File("people/doctor.png"));
				with open("linelock/puzzle.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
				with open("linelock/whip.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			elif cls == 10:
				with open("linelock/kidnap.txt", 'r') as file:
					file_content = file.read()
				await put_channel.send(file_content);
			else:
				msg.channel.send(can[2]);
				return;
	except Exception as e:
		print(e);
		await msg.channel.send(can[1]);
if __name__ == "__main__":
	bot.run(T);
