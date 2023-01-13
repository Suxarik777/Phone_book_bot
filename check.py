


def input_new_number_new_row(array):
    new_number_row = what_is_row_new_database_entry(array)
    last_index = len(array) - 1
    last_sub_list = array[last_index]

    new_sub_list = forced_recording_number_row_database(last_sub_list, new_number_row)

    array.insert(0, new_sub_list)
    return array



# вспомогательные функции для записи базы
# поиск нового номера строки в базе для новой записи
def what_is_row_new_database_entry(array):
    # last_index_row = len(array) - 1
    last_row_index = len(array) - 2 # потому, что последняя запись от пользователя без номера
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