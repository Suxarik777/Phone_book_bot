from telebot import TeleBot, types


def bot_mess_start(msg):
    bot_mess: str = f'''Привет, <b>{msg.from_user.first_name} {msg.from_user.last_name}</b>
Я создан студентом GeekBrains и я телефонная книжка
ЖМИ кнопку "Меню"'''
    return bot_mess


def bot_mess_menu():
    bot_mess: str = 'Что будем делать?'
    return bot_mess


def bot_mess_input():
    bot_mess: str = 'Как ты хочешь ввести данные'
    return bot_mess

def bot_mess_keyboard_input():
    bot_mess: str = 'Введите данные в формате ' \
                    '\nИмя Фамилия Телефон Комментарий'
    return bot_mess
