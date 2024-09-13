import discord
T = open("token.txt", 'r').read();
ints = discord.Intents.all();
bot = discord.Client(intents = ints);
male_sea = 1270754183896633357;
one_class = 1270768845858279445;
report = [1282572034777415720, 1282572337698312193, 1282572398545211454, 1282572465549217833, 1282572564409094187, 1282572666376683572, 1282572732717994045, 1282572797096493127, 1282572894756540460, 1283891292748775495, 1282572941543997440, 1282573032866451466];
channel_id = [114514, 1284040592053108736, 1284040868042506241, 1284041111861727233, 1270782049053315132, 1270783094890172538, 1270783334620074056, 1270785759707791472, 1270786026755067997, 1270786823400063076];
call_cnt = [];
max_cnt = [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 2];
closecard = {"信徒的話" : 3, "藍菈娜的故事" : 5, "獻祭儀式" : 6, "廢棄倉庫的冤魂" : 11};
can = ["並沒有", "不要瞎掰好嗎", "這顯然是廠商的疏失"];
def ran_can():
	return 
@bot.event
async def on_ready():
	for i in range(0, 12):
		call_cnt.append([]);
		for j in range(0, 12):
			call_cnt[i].append(0);
	print("logged in as", end = ' ');
	print(bot.user);
@bot.event
async def on_message(msg : discord.Message):
	if msg.author == bot.user or msg.channel.id == one_class or msg.channel.id == male_sea:
		return;
	try:
		grp = 0;
		cls = 0;
		for i in range(0, 12):
			if msg.channel.id == report[i]:
				if msg.content[0] == 'd' and msg.content[2] == 'b' and msg.content[1] >= '1' and msg.content[1] <= '9':
					tmp = ord(msg.content[1]) ^ 48;
					if(call_cnt[tmp][i] == 0):
						call_cnt[tmp][i] = 1;
						grp = tmp;
						cls = i;
		if grp == 0:
			cc = closecard[msg.content];
			for i in range(1, 10):
				if msg.channel.id == channel_id[i]:
					if call_cnt[i][cc] == 1 and max_cnt[cc] == 2:
						call_cnt[i][cc] = 2;
						grp = i;
						cls = cc;
					else:
						await msg.channel.send(can[0]);
						return;
		if grp == 0:
			return;
		if call_cnt[grp][cls] == max_cnt[cls]:
			put_channel = bot.get_channel(channel_id[grp]);	
		else:
			return;
		if cls == 0:
			await put_channel.send(file = discord.File("map/map.jpg"));
			with open("map/close_card.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			with open("people/yourself.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			with open("people/another_me.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("people/small_fire.png"));
			with open("people/aranara.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("people/aranara.png"));
			with open("linelock/pre.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
		elif cls == 1:
			with open("people/police.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("people/police.png"));
			await put_channel.send(file = discord.File("linelock/star.jpg"));
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
			await put_channel.send(file = discord.File("linelock/genshin.png"));
			with open("linelock/AC.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
		elif cls == 4:
			with open("linelock/dead_body.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("linelock/dead_body.jpg"));
		elif cls == 5:
			with open("linelock/turtle_soup.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
		elif cls == 6:
			with open("people/Gsus.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("people/Gsus.png"));
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
			await put_channel.send(file = discord.File("people/lorenzo.png"));
			with open("linelock/wierd_aranara.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			with open("linelock/de_aranara.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("linelock/dance.png"));
		elif cls == 9:
			with open("linelock/dance.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
		elif cls == 10:
			with open("people/doctor.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("people/doctor.png"));
			with open("linelock/puzzle.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("linelock/puzzle.jpg"));
			with open("linelock/whip.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
		elif cls == 11:
			with open("people/ghost.txt", 'r') as file:
				file_content = file.read()
			await put_channel.send(file_content);
			await put_channel.send(file = discord.File("people/ghost.jpg"));
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
