# -*- coding: utf8 -*-
import telebot

bot = telebot.TeleBot('1495506119:AAF_ZyrAlBSU4_9anJKHLVMBukjB2YAzC50')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет привет ')


bot.polling()