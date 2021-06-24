from decouple import config
from responses import *
import telebot

"""
Prerequisites:

Install pyTelegramBotAPI, python-decouple libraries. 

"""

API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey!")


@bot.message_handler(regexp='Date')
def date(message):
    bot.send_message(message.chat.id, date_fn())


@bot.message_handler(regexp='Time')
def time(message):
    bot.send_message(message.chat.id, time_fn())


@bot.message_handler(regexp='Weather')
def weather(message):
    bot.send_message(message.chat.id, weather_fn())


@bot.message_handler(regexp='Trending Songs')
def trending_music(message):
    bot.send_message(message.chat.id, trending_songs_fn())


@bot.message_handler(regexp='Trending Albums')
def trending_albums(message):
    bot.send_message(message.chat.id, hot_albums_fn())


@bot.message_handler(regexp='ICT Jobs')
def ict_jobs(message):
    bot.send_message(message.chat.id, vacancy_mail_ict_jobs())


# Echos all messages except known ones. Keep it at the bottom
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
