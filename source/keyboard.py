from telebot import types

def weather_search_button():
    '''
    Returns a button for requesting a weather search in a city
    '''

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    item1 = types.KeyboardButton("-- 🌍🔍--")

    markup.add(item1)

    return markup