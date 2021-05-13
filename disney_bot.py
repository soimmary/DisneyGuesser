import telebot
import conf

bot = telebot.TeleBot(conf.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет! Это бот, который угадывает персонажей диснеевских мультфильмов по репликам 🦄🌟\n Введи реплику!")


@bot.message_handler(func=lambda m: True)
def send_len(message):
    bot.send_message(message.chat.id,
                     'В вашем сообщении {} символов.'.format(len(message.text)))


if __name__ == '__main__':
    bot.polling(none_stop=True)
