from func_for_file import read_file, recording_file

def delete_row(dct_lst_user_id):
    number_str = dct_lst_user_id[0]
    data_array = read_file()
    if number_str.isdigit:
        index = int(number_str) - 1
        if index < len(data_array):
            del data_array[index]
            recording_file(data_array)
            bot_mess = 'Запись удалена'
            return bot_mess
        else:
            bot_mess = 'Упс, что-то не так'
            return bot_mess
    else:
        bot_mess = 'Вы ввели не число'
        return bot_mess


def update_row(row_str, text):
    sub_lst = text.split()
    data_array = read_file()

    index = int(row_str) - 1
    del data_array[index]
    data_array.insert(index, sub_lst)

    return data_array