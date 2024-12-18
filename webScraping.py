import requests
from bs4 import BeautifulSoup
import telebot
import html
from telebot import types

bot = telebot.TeleBot("7875859722:AAG8WqtBphLBrr3KjKWEkO18Zs6Yr3zkoCs")
bot.parse_mode = "HTML"


def get_link():
	URL = "https://kusonime.com/arcane-s2-batch-subtitle-indonesia/"
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, "html.parser")
	recommendation = soup.select('#rekomendednim > a:nth-child(2)')[0]["href"]

	return recommendation


cmds = [
	"/start - Display commands list",
	"/anime - Recommends an Anime",
	"/search (content) - Search Anime"
	]

cmd_list = "\n".join(cmds)



@bot.message_handler(commands=['start'])
def display_commands(message):
	bot.reply_to(message, cmd_list)



@bot.message_handler(regexp='\/search \w+')
def ask_anime(message):
	search = str(message.text)
	search = search.replace("/search", "")
	URL = f"https://kusonime.com/?s={search}&post_type=post"
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, "html.parser")
	tes = soup.select('#venkonten > div.vezone > div.venser > div > div > div.rseries > div.rapi > div > ul > div:nth-child(1) > div > div.content > h2 > a')
	tes = tes[0]["href"]
	
	URL = tes
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, "html.parser")

	#															IMAGE
	image = soup.select('#venkonten > div.vezone > div.venser > div.post-thumb > img')[0]["src"]
	print(image)

	#															TITLE
	title = soup.select('#venkonten > div.vezone > div.venser > div.post-thumb > h1')
	title = soup.title.string

	#															DESCRIPTION
	description = soup.select('#venkonten > div.vezone > div.venser > div.venutama > div.lexot > p:nth-child(3)')[0].get_text()
	
	#				--------------------------------------------TEXT--------------------------------------------
	text = f"<blockquote>{title}</blockquote>\n\n"			  
	text += f"{description}"
	#				--------------------------------------------------------------------------------------------

	#				-------------------------------------------BUTTON---------------------------------------------
	button_web = types.InlineKeyboardButton('Go To Website', url = URL)
	#				--------------------------------------------------------------------------------------------

	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(button_web)

	bot.send_photo(message.chat.id, image, text, reply_markup=keyboard)

		


@bot.message_handler(commands=['anime'])
def recommend_anime(message):
	URL = get_link()
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, "html.parser")

	#															IMAGE
	image = soup.select('#venkonten > div.vezone > div.venser > div.post-thumb > img')[0]["src"]
	print(image)

	#															TITLE
	title = soup.select('#venkonten > div.vezone > div.venser > div.post-thumb > h1')
	title = soup.title.string

	#															DESCRIPTION
	description = soup.select('#venkonten > div.vezone > div.venser > div.venutama > div.lexot > p:nth-child(3)')[0].get_text()
	
	#				--------------------------------------------TEXT--------------------------------------------
	text = f"<blockquote>{title}</blockquote>\n\n"			  
	text += f"{description}"
	#				--------------------------------------------------------------------------------------------

	#				-------------------------------------------BUTTON---------------------------------------------
	button_web = types.InlineKeyboardButton('Go To Website', url = URL)
	#				--------------------------------------------------------------------------------------------

	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(button_web)

	bot.send_photo(message.chat.id, image, text, reply_markup=keyboard)




bot.infinity_polling()