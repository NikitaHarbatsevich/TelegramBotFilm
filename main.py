import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup

HEADERS = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
BASE_URL = "https://kinokrad.cc"

all_films = []


def parce_all_films():
        response = requests.get(f"{BASE_URL}/3-uzhasy/")
        soup = BeautifulSoup(response.content, "html.parser")
        items = soup.find_all("div", class_ = "shorbox")
        for item in items:

            all_films.append(
                {
                    "movie_title" : item.find("a").text,
                    "link" : item.find("a").get("href"),
                    "year_of_issue" : item.find("div", class_ = "item year").text.__str__().split("\n")[2],
                    "image" : f'https://kinokrad.cc{item.find("div", class_ = "postershort").find("img").get("data-src")}'
                }
            )

c = parce_all_films()
print(all_films)

bot = telebot.TeleBot("6053934657:AAGIRYaXbzD5kbdTOsdl6exoURR_qJq71pw")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать фильм по названию")
    btn2 = types.KeyboardButton("Выбрать фильм по актеру")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name} {message.from_user.last_name}!, меня зовут TeleFilm bot.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Выбрать фильм по названию"):

        bot.send_message(message.chat.id, text="Пишите название")





bot.polling(none_stop=True)

