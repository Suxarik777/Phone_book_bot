import csv


def read_file():
    with open('data_base.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        array = []
        for line, row in enumerate(file_reader):
            # if line>1:
            file_reader_to_list = (';'.join(row)).split(';')
            array.append(file_reader_to_list)
        return array


def recording_file(array):
    with open(f'data_base.csv', 'w', encoding='utf-8') as file:
        for text in array:
            res_text = ";".join(text)
            file.writelines(f'{res_text}\n')


