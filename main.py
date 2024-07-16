from random import randint

from bs4 import BeautifulSoup
import requests

def get_anecdot():
    # создаем url сайта
    url = f'https://www.anekdot.ru/last/anekdot/'
    # делаем запрос
    response = requests.get(url)
    # создаем объект "красивый суп"
    soup = BeautifulSoup(response.text, 'html.parser')

    # используем метод findAll, для поиска нужного HTML тега
    # метод findAll возвращает HTML заключеный в этот тег
    answer = soup.findAll('div', class_='text')

    #возвращаем список HTML блоков
    return answer

import telebot
from telebot.types import ReplyKeyboardMarkup

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7071800191:AAGIs28xt9bsQonvemOezuxjG0K1M9U9nGI')

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    murkup = ReplyKeyboardMarkup()
    murkup.add('Случайный анекдот')
    bot.send_message(message.chat.id, "Пожалуйста, отправьте слово значение которого хотите узнать.", reply_markup=murkup)

# Обработка всех сообщений
@bot.message_handler(func=lambda callback: True)
def handle_location(message):
    try:
        answer = get_anecdot()
        bot.send_message(message.chat.id, answer[randint(0, len(answer))].text)
    except:
        bot.send_message(message.chat.id, 'Извините я вас не понял')

# Запуск бота
bot.polling()