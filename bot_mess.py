from func_for_file import read_file


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

def bot_mess_file_input():
    bot_mess: str = 'Выберите формат загружаемого файла'
    return bot_mess

def bot_mess_view_all():
    data_array = read_file()
    bot_mess: str = ''
    for i in range(len(data_array)):
        row = ' '.join(data_array[i])
        bot_mess += row + '\n'
    return bot_mess


def bot_mess_view_row(index_row):
    data_array = read_file()
    bot_mess: str = ''
    if index_row < len(data_array):
        bot_mess = ' '.join(data_array[index_row])
    else:
        bot_mess = 'Такой записи нету'
    return bot_mess


def bot_mess_view_row_filter(text):
    data_array = read_file()
    bot_mess: str = ''
    for line in range(len(data_array)):
        for row in range(len(data_array[line])):
            # print(arr[line][row])
            if data_array[line][row].find(text) > -1:
                show_row = ' '.join(data_array[line])
                bot_mess += f'{show_row}\n'
    return bot_mess