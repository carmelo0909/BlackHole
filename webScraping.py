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




@bot.message_handler(commands=['start'])
def send_welcome(message):
	URL = get_link()
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, "html.parser")

	#															IMAGE
	image = soup.select('#venkonten > div.vezone > div.venser > div.post-thumb > img')[0]["src"]
	print(image)

	#															TITLE
	title = soup.select('#venkonten > div.vezone > div.venser > div.post-thumb > h1')    #Judul
	title = soup.title.string

	#															DESCRIPTION
	description = soup.select('#venkonten > div.vezone > div.venser > div.venutama > div.lexot > p:nth-child(3)')[0].get_text()    #Description
	
	#															TEXT v
	text = f"<blockquote>{title}</blockquote>\n\n"			  
	text += f"{description}"
	#															^ TEXT



	button_foo = types.InlineKeyboardButton('Go To Website', url = URL)
	button_bar = types.InlineKeyboardButton('Shuffle', url = URL)

	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(button_foo)
	keyboard.add(button_bar)

	bot.send_photo(message.chat.id, image, text, reply_markup=keyboard)


bot.infinity_polling()