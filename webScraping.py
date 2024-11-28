import requests
from bs4 import BeautifulSoup, NavigableString
from lxml import etree
import telebot

bot = telebot.TeleBot("7875859722:AAG8WqtBphLBrr3KjKWEkO18Zs6Yr3zkoCs")


URL = "https://kusonime.com/arcane-s2-batch-subtitle-indonesia/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")


title = soup.select('#venkonten > div.vezone > div.venser > div.post-thumb > h1')    #Judul
title = soup.title.string

dom = etree.HTML(str(soup))
description = dom.xpath('//*[@id="venkonten"]/div[7]/div[1]/div[3]/div[2]/p[1]')[0]    #Description

print(title)
print(description)



@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.parse_mode = "HTML"
	bot.reply_to(message, f"""<blockquote>{title}</blockquote>
			  
{description}""")


bot.infinity_polling()