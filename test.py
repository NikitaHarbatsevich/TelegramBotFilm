import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup

page = 2
filter_list = []




    URL = f"https://hd-rezka.biz/filmy/page/{page}/"
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    movie_title = soup.find(class_="b-content__inline_items not-home").find_all("a")
    if len(movie_title):
        #filter_list.append(movie_title[index])
        page += 1
    else:
        break


bot = telebot.TeleBot("6053934657:AAGIRYaXbzD5kbdTOsdl6exoURR_qJq71pw")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать фильм по названию")
    btn2 = types.KeyboardButton("Выбрать фильм по актеру")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name} {message.from_user.last_name}!, меня зовут TeleFilm bot, моя задача найти фильм который ты хочешь посмотреть.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Выбрать фильм по названию"):

        bot.send_message(message.chat.id, text="Пишите название")





bot.polling(none_stop=True)

