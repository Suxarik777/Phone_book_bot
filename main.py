# pip and func
from telebot import TeleBot, types
from config import TOKEN_ID
import emoji
import os
from bot_mess import bot_mess_start, bot_mess_menu, bot_mess_input, bot_mess_keyboard_input, \
    bot_mess_file_input, bot_mess_view_all, bot_mess_view_row, bot_mess_view_row_filter, \
    bot_mess_edit, bot_mess_edit_two_step
from button import but_start_menu, but_menu, but_inline_init, but_inline_format_file, but_inline_view, \
    but_inline_edit_two_step, but_inline_export
from func_for_file import read_file, recording_file
from input import input_keyboard, input_file_user_to_array, input_new_array_user_to_data_array
from edit import delete_row, update_row
from export import export_csv, export_html, export_xml
from check import input_new_number_new_row


#

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)

os.chdir(os.path.dirname(__file__))

dct = {}

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

    if msg.text == emoji.emojize(':writing_hand: Ввести данные'): # input
        bot.send_message(chat_id=msg.chat.id, text=bot_mess_input(), parse_mode='html',
                         reply_markup=but_inline_init())

    if msg.text == emoji.emojize(':backhand_index_pointing_right: Редактировать'): # edit
        dct[msg.from_user.id] = []  # при переходе в меню по его айди словарика кладём/обнуляем пустой список

        msg = bot.send_message(chat_id=msg.chat.id, text=bot_mess_edit(), parse_mode='html')
        bot.register_next_step_handler(msg, edit_two_step)

    if msg.text == emoji.emojize(':card_index_dividers: Экспорт в файл'):
        bot.send_message(chat_id=msg.chat.id, text='Выберите формат', reply_markup=but_inline_export())



# меню 2 уровня edit
def edit_two_step(msg: types.Message):
    row_number_str = msg.text
    id_= msg.from_user.id
    dct[id_].append(row_number_str)

    bot.send_message(chat_id=msg.chat.id, text=bot_mess_edit_two_step(row_number_str),
                         parse_mode='html', reply_markup=but_inline_edit_two_step())


@bot.callback_query_handler(func=lambda call: True)
def callback_init(call: types.CallbackQuery):
    # обработка view
    if call.data == 'номер записи':
        msg = bot.send_message(chat_id=call.message.chat.id, text='Введите номер строки записи')
        bot.register_next_step_handler(msg, view_row_index)

    if call.data == 'искать':
        msg = bot.send_message(chat_id=call.message.chat.id, text='Введите слово или номер по которому ищем')
        bot.register_next_step_handler(msg, view_row_search_filter)


    if call.data == 'смотреть всех':
        bot.send_message(chat_id=call.message.chat.id, text=bot_mess_view_all(),
                         reply_markup=but_menu())

    # обработка input
    if call.data == 'с клавиатуры':
        msg = bot.send_message(chat_id=call.message.chat.id, text=bot_mess_keyboard_input())
        bot.register_next_step_handler(msg, recording_str_keyboard)
        # в обработку текста в Сall, функция ниже

    if call.data == 'из файла':
        bot.send_message(chat_id=call.message.chat.id, text=bot_mess_file_input(),
                         reply_markup=but_inline_format_file())

    # 2 шаг input 'из файла'
    if call.data == 'csv':
        msg = bot.send_message(chat_id=call.message.chat.id, text='Загрузите файл в формате .csv',
                               reply_markup=but_menu())
        bot.register_next_step_handler(msg, read_csv_file_user)

    if call.data == 'html':
        bot.send_message(chat_id=call.message.chat.id, text=emoji.emojize('Пока не доступно.'
                                                            '\nТолько не говорите преподавателю '
                                                            ':shushing_face:'),
                         reply_markup=but_menu())

    # обработка edit второй шаг
    if call.data == 'удалить':
        id_ = call.from_user.id

        bot_mess = delete_row(dct[id_])  # func from edit
        bot.send_message(chat_id=call.message.chat.id, text=bot_mess,
                         reply_markup=but_menu())

    if call.data == 'редактировать':
        msg = bot.send_message(chat_id=call.message.chat.id, text=bot_mess_keyboard_input(),
                         reply_markup=but_menu())
        bot.register_next_step_handler(msg, update_str_keyboard)

    # export
    if call.data == 'csv_export':
        name_file = 'data_base_request_user'
        export_csv(name_file)
        csv_doc = open(f'{name_file}.csv', 'rb')
        bot.send_document(chat_id=call.message.chat.id, document=csv_doc)

    if call.data == 'html_export':
        name_file = 'data_base_request_user'
        export_html(name_file)
        html_doc = open(f'{name_file}.html', 'rb')
        bot.send_document(chat_id=call.message.chat.id, document=html_doc)

    if call.data == 'xml_export':
        name_file = 'data_base_request_user'
        export_xml(name_file)
        xml_doc = open(f'{name_file}.xml', 'rb')
        bot.send_document(chat_id=call.message.chat.id, document=xml_doc)

# 2 шаг после view 'номер записи'
def view_row_index(msg: types.Message):
    number_row = msg.text

    if number_row.isdigit():
        index_row = int(number_row) - 1
        bot.send_message(chat_id=msg.chat.id, text=bot_mess_view_row(index_row),
                         reply_markup=but_menu())
    else:
        bot.send_message(chat_id=msg.chat.id, text='Что-то пошло не так!'
                                                   '\nНаверное вы указали не число',
                         reply_markup=but_menu())


# 2 шаг после view 'искать'
def view_row_search_filter(msg: types.Message):
    text = str(msg.text)
    bot.send_message(chat_id=msg.chat.id, text=bot_mess_view_row_filter(text), reply_markup=but_menu())


# 2 шаг после input 'с клавиатуры' - результат
def recording_str_keyboard(msg: types.Message):
    data_array = input_keyboard(str(msg))
    recording_file(data_array)

    bot.send_message(chat_id=msg.chat.id, text='Новые данные записаны', reply_markup=but_menu())


# 3 шаг edit редактирова
def update_str_keyboard(msg: types.Message):
    text = msg.text
    dct_user_id_lst = dct[msg.from_user.id]
    index_str = dct_user_id_lst[0]

    data_array = update_row(index_str, text)
    recording_file(data_array)

    bot.send_message(chat_id=msg.chat.id, text='Данные обновлены', reply_markup=but_menu())

# 3 шаг input из файла
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