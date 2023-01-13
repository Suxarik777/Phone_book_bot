# pip and func
from telebot import TeleBot, types
from config import TOKEN_ID
import emoji
import os
from bot_mess import bot_mess_start, bot_mess_menu, bot_mess_input, bot_mess_keyboard_input, \
    bot_mess_file_input, bot_mess_view_all
from button import but_start_menu, but_menu, but_inline_init, but_inline_format_file, but_inline_view
from func_for_file import read_file, recording_file
from input import input_keyboard, input_file_user_to_array, input_new_array_user_to_data_array
from check import input_new_number_new_row


#

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)

os.chdir(os.path.dirname(__file__))

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
    if msg.text == emoji.emojize(':eyes: Посмотреть данные'): # view
        bot.send_message(chat_id=msg.chat.id, text='Что посмотрим', reply_markup=but_inline_view())

    if msg.text == emoji.emojize(':writing_hand: Ввести данные'): # init
        bot.send_message(chat_id=msg.chat.id, text=bot_mess_input(), parse_mode='html',
                         reply_markup=but_inline_init())



@bot.callback_query_handler(func=lambda call: True)
def callback_init(call: types.CallbackQuery):
    # обработка view
    if call.data == 'номер записи':
        bot.send_message(chat_id=call.message.chat.id, text='УПС.\n В разработке')

    if call.data == 'искать':
        bot.send_message(chat_id=call.message.chat.id, text='УПС.\n В разработке')

    if call.data == 'смотреть всех':
        bot.send_message(chat_id=call.message.chat.id, text=bot_mess_view_all(),
                         reply_markup=but_menu())

    # обработка init
    if call.data == 'с клавиатуры':
        msg = bot.send_message(chat_id=call.message.chat.id, text=bot_mess_keyboard_input())
        bot.register_next_step_handler(msg, recording_str_keyboard)
        # в обработку текста в Сall, функция ниже

    if call.data == 'из файла':
        bot.send_message(chat_id=call.message.chat.id, text=bot_mess_file_input(),
                               reply_markup=but_inline_format_file())

    # 2 шаг 'из файла'
    if call.data == 'csv':
        msg = bot.send_message(chat_id=call.message.chat.id, text='Загрузите файл в формате .csv',
                               reply_markup=but_menu())
        bot.register_next_step_handler(msg, read_csv_file_user)

    if call.data == 'html':
        bot.send_message(chat_id=call.message.chat.id, text='Пока не доступно.'
                                                            '\n только не говорите преподавателю '
                                                            ':shushing_face:',
                         reply_markup=but_menu())


# 2 шаг после 'с клавиатуры' - результат
def recording_str_keyboard(msg: types.Message):
    data_array = input_keyboard(str(msg))
    recording_file(data_array)

    bot.send_message(chat_id=msg.chat.id, text='Новые данные записаны', reply_markup=but_menu())




@bot.message_handler(content_types=['documents'])
def read_csv_file_user(msg: types.Message):
    file_name = msg.document.file_name

    with open(file_name, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))

    new_array_user = input_file_user_to_array(file_name)
    data_array = input_new_array_user_to_data_array(new_array_user)

    recording_file(data_array)

    bot.send_message(chat_id=msg.chat.id, text=emoji.emojize('Файл принят, данные записаны :OK_hand:'),
                     reply_markup=but_menu())





bot.polling(none_stop=True)