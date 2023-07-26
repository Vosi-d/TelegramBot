from telebot import types

def choice_buttons():
    #Sozdayom prostranstvo dly knopok
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #Sozdayom sami knopki
    wiki = types.KeyboardButton('Vikipedia')
    translate = types.KeyboardButton('Translator')
    #Dobovlyayem knopki v prostranstvo
    kb.add(wiki, translate)

    return kb