import telebot
import buttons as bt
#Registrasiya token
bot = telebot.TeleBot('6411108341:AAHGW1akR44YbzmffuyVHA0io9SR6Lmrzo8')

#Propisovaem algoritm Komanda/start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,'Welcome ',reply_markup=bt.choice_buttons())
#Zapusk bot

@bot.message_handler(content_types=['text'])
def text_message (message):
    if message.text.lower() == 'vikipedia':
        bot.send_message(message.from_user.id,'Enter text')
        bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == 'translator':
        bot.send_message(message.from_user.id,'Enter text for translate')
        bot.register_next_step_handler(message, translate)
    else:
        bot.send_message(message.from_user.id,'I do not understand you')

bot.polling(non_stop=True)
