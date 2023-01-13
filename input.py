from func_for_file import read_file, recording_file
import csv


def input_keyboard(text):
    data_sub_list = text.split()
    data_array = read_file()
    data_array.append(data_sub_list)
    data_array = input_new_number_new_row(data_array)  # впиши новый номер строки последней строки
    return data_array


def input_file_user_to_array(file_user):
    with open(file_user, 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=' ', skipinitialspace=False)
        data_array = []
        for line, row in enumerate(file_reader):
            file_reader_row_to_list = (';'.join(row)).split(';')
            data_array.append(file_reader_row_to_list)

    return data_array


def input_new_array_user_to_data_array(new_array_user):
    data_array = read_file()
    for line in new_array_user:
        data_array.append(line)
    return data_array


# Функции 2 шага обработки
def input_new_number_new_row(array):
    new_number_row = what_is_row_new_database_entry(array)
    last_index = len(array) - 1
    last_sub_list = array[last_index]

    new_sub_list = forced_recording_number_row_database(last_sub_list, new_number_row)

    array.insert(0, new_sub_list)
    return array

# не реализовано
# def input_new_numbers_new_row_is_file(array, new_array_user):
#     new_numbers_row = what_is_row_new_database_entry(array, new_array_user)
#     last_index = len(array) - 1
#     last_sub_list = array[last_index]
#
#     new_sub_list = forced_recording_number_row_database(last_sub_list, new_number_row)
#
#     array.insert(0, new_sub_list)
#     return array

# вспомогательные функции для записи базы
# поиск нового номера строки в базе для новой записи
def what_is_row_new_database_entry(array):
    # last_index_row = len(array) - 1
    last_row_index = len(array) - 2  # потому, что последняя запись от пользователя без номера
    last_number_user = int(array[last_row_index][0])

    next_number_user = last_number_user + 1
    return next_number_user


def forced_recording_number_row_database(sub_lst, number):
    str_sub_lst = ' '.join(map(str, sub_lst))
    print(f'проверяем порядковый номер записи: \n{str_sub_lst} \nприсваиваем номер: {number}')
    # if sub_lst[0].isdigit:
    #     sub_lst[0] = str(number)
    #     return sub_lst
    # else:
    sub_lst.insert(0, str(number))
    print(sub_lst)
    return sub_lst