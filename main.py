from telebot import TeleBot, types
from config import TOKEN_ID

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_program(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # растяни по ширине экрана и добавь две кнопк
    button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
    markup.add(button_menu)

    mess = f'''Привет, <b>{msg.from_user.first_name} {msg.from_user.last_name}</b>
Я создан студентом GeekBrains и я телефонная книжка
ЖМИ кнопку "Меню"'''
    bot.send_message(chat_id=msg.chat.id, text=mess, parse_mode='html', reply_markup=markup)
