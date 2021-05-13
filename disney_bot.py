import telebot
import os
import pandas as pd
import numpy as np
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

sw = stopwords.words('russian')
stemmer = SnowballStemmer('russian')


def custom_tokenizer(text):
    return [stemmer.stem(w) for w in word_tokenize(text.lower(), language='russian') if w.isalpha() and not w in sw]


vectorizer = load('vectorizer.joblib')
clf = load('clf.joblib')


def answer(text):
  a = clf.predict(vectorizer.transform([text])).tolist()[0]
  if a == "PRINCESS":
    return "You are a princess!"
  elif a == "PRINCE":
    return "You are a prince."
  else:
    return "You are a side character:("


""" Подключаем бота """

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет! Это бот, который угадывает персонажей диснеевских "
                     "мультфильмов по репликам 🦄🌟\nВведи реплику!")


@bot.message_handler(func=lambda m: True)
def send_result(message):
    bot.send_message(answer(message.chat.id))


if __name__ == '__main__':
    bot.polling(none_stop=True)
