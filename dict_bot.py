import requests
from bs4 import BeautifulSoup


def get_info_word(word):

    # создаем url сайта
    url = f'https://ru.wiktionary.org/wiki/{word}'
    # делаем запрос
    response = requests.get(url)
    # создаем объект "красивый суп"
    soup = BeautifulSoup(response.text, 'html.parser')

    # используем метод find, для поиска нужного HTML тега
    # метод find возвращает HTML заключеный в этот тег
    answer = soup.find('ol')

    #возвращаем текст из HTML блока
    return answer.text

import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot(token)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Пожалуйста, отправьте слово значение которого хотите узнать.")

# Обработка всех сообщений
@bot.message_handler(func=lambda callback: True)
def handle_location(message):
    try:
        answer = get_info_word(message.text)
        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, 'Извините я вас не понял')

# Запуск бота
bot.polling()

