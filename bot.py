from secret import api_key, api_secret, bot_key
import telebot
from binance_utils import *

bot = telebot.TeleBot(bot_key)
client = Client(api_key, api_secret)


@bot.message_handler(commands=['help'])
def help_message(message):
    '''
    This function adds a selection menu to the telegram channel.
    :param message: /help
    :return:
    '''
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('RUB', 'USD')
    bot.send_message(message.chat.id, 'At the moment, on your account ...', reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start_message(message):
    '''
    This function displays the welcome message of the Bot using the /start command.
    :param message: /start
    :return:
    '''
    bot.send_message(message.chat.id,
                     'Hi! I am a Bot that shows the amount of remaining funds in your Binance account !')
    help_message(message)


@bot.message_handler(content_types=['text'])
def send_text(message):
    '''
    This function displays the account balance by selecting the currency in the selection menu.
    :param message: RUB, USD
    :return:
    '''
    if message.text.lower() == 'RUB'.lower():
        bot.send_message(message.chat.id, 'At the moment, you have  ' + str(
            get_status_in_val(client, 'ETHRUB')) + ' RUB on your account at the rate of '
                         + str(get_ex_coin(client, 'ETHRUB')) + ' for 1 coin!')
    elif message.text.lower() == 'USD'.lower():
        bot.send_message(message.chat.id, 'At the moment, you have ' + str(
            get_status_in_val(client, 'ETHUSDT')) + ' USD on your account at the rate of '
                         + str(get_ex_coin(client, 'ETHRUB')) + ' for 1 coin!')
    else:
        bot.send_message(message.chat.id, 'What do you want?')


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
