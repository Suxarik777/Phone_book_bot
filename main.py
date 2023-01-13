# pip and func
from telebot import TeleBot, types
from config import TOKEN_ID
import emoji
from bot_mess import bot_mess_start, bot_mess_menu, bot_mess_input, bot_mess_keyboard_input
from button import but_start_menu, but_menu, but_inline_init
from func_for_file import read_file, recording_file
from check import input_new_number_new_row

#

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_program(msg: types.Message):
    bot.send_message(chat_id=msg.chat.id, text=bot_mess_start(msg), parse_mode='html',
                     reply_markup=but_start_menu())


@bot.message_handler(content_types=['text'])
def menu(msg: types.Message):
    # Главное меню
    if msg.text == emoji.emojize(':scroll: Меню'):
        bot.send_message(chat_id=msg.chat.id, text=bot_mess_menu(), parse_mode='html',
                         reply_markup=but_menu())

    # Меню 2 уровня
    if msg.text == emoji.emojize(':writing_hand: Ввести данные'): # init
        bot.send_message(chat_id=msg.chat.id, text=bot_mess_input(), parse_mode='html',
                         reply_markup=but_inline_init())


@bot.callback_query_handler(func=lambda call: True)
def callback_init(call: types.CallbackQuery):
    if call.data == 'с клавиатуры':
        msg = bot.send_message(chat_id=call.message.chat.id, text=bot_mess_keyboard_input())
        bot.register_next_step_handler(msg, recording_str_keyboard)


def recording_str_keyboard(msg: types.Message):
    text = str(msg.text)

    data_sub_list = text.split()
    data_array = read_file()
    data_array.append(data_sub_list)
    data_array = input_new_number_new_row(data_array)  # впиши новый номер строки последней строки
    recording_file(data_array)

    bot.send_message(chat_id=msg.chat.id, text='Новые данные записаны', reply_markup=but_menu())








bot.polling(none_stop=True)