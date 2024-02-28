from config import token
from weather import weather_message
from translation import translate_message

import telebot
from telebot import types

# Getting a bot token
bot = telebot.TeleBot(token)

# Keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('/weather')


@bot.message_handler(commands=['start'])
def send_welcome(message):

    language = message.from_user.language_code

    welcome_message = "Hi"
    message_for_user = "Click on the button to start interacting with the bot"

    if language != "en":
        welcome_message = translate_message(welcome_message, language)
        message_for_user = translate_message(message_for_user, language)

    msg = bot.send_message(message.chat.id, f"{welcome_message}, {message.from_user.first_name}! \n\n" +
                           message_for_user, reply_markup=markup)


@bot.message_handler(commands=['weather'])
def weather(message):

    language = message.from_user.language_code

    message_for_user = "Write your city:"

    if language != "en":
        message_for_user = translate_message(message_for_user, language)

    msg = bot.send_message(message.chat.id, message_for_user)

    bot.register_next_step_handler(msg, current_weather)


def current_weather(message):

    try:

        chat_id = message.chat.id
        language = message.from_user.language_code

        city = message.text
 
        weather_info, icon = weather_message(city)

        if language != "en":
            weather_info = translate_message(weather_info, language)

        bot.send_photo(message.chat.id, icon, weather_info, parse_mode="Markdown", reply_markup=markup)
    
    except Exception as e:

        language = message.from_user.language_code

        message_for_user = "There is no such city on the list. Try again"

        if language != "en":
            message_for_user = translate_message(message_for_user, language)

        bot.send_message(message.chat.id, message_for_user, reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)