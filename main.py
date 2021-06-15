from decouple import config
from responses import time_fn, date_fn
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


@bot.message_handler(commands=['Date'])
def date(message):
    bot.send_message(message.chat.id, date_fn())


@bot.message_handler(commands=['Time'])
def time(message):
    bot.send_message(message.chat.id, time_fn())


bot.polling()
