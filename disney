import telebot


TOKEN = '1702534397:AAECFdJJJe7teEB0P06vFIx4HgQSUWTO82o'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте! Это бот, который считает длину вашего сообщения.")


@bot.message_handler(func=lambda m: True)
def send_len(message):
    bot.send_message(message.chat.id,
                     'В вашем сообщении {} символов.'.format(len(message.text)))


if __name__ == '__main__':
    bot.polling(none_stop=True)
