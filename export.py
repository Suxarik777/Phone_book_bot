import os
os.chdir(os.path.dirname(__file__))
from xml.etree import ElementTree as ET
from func_for_file import read_file


def export_csv(name_file):
    arr = read_file()

    with open(f'{name_file}.csv', 'w', encoding='utf-8') as file:
        for text in arr:
            res_text = ";".join(text)
            file.writelines(f'{res_text}; \n')


def export_xml(name_file):
    arr = read_file()

    Phone_Book = ET.Element('Phone_Book')
    for item in arr:
        user = ET.SubElement(Phone_Book, f'user')
        surname = ET.SubElement(user, 'surname')
        surname.text = item[0]
        name = ET.SubElement(user, 'name')
        name.text = item[1]
        telephone = ET.SubElement(user, 'telephone')
        telephone.text = item[2]
        comments = ET.SubElement(user, 'comments')
        comments.text = item[3]
    data = ET.tostring(Phone_Book, encoding='unicode')
    file = open(f'{name_file}.xml', 'w', encoding='utf-8')
    file.writelines(data)



def export_html(name_file):
    arr = read_file()
    with open(f'{name_file}.html', 'w', encoding='utf-8') as file:
        file.writelines(f'<!DOCTYPE html>\n')
        file.writelines(f'<html lang="ru">\n')
        file.writelines(f'\t<head>\n')
        file.writelines(f'\t\t<meta charset="utf-8">\n')
        file.writelines(f'\t\t<title>Phone Book</title>\n')
        file.writelines(f'\t<head>\n')
        file.writelines(f'\n')
        file.writelines(f'\t<body>\n')
        file.writelines(f'\t\t<h2>Phone Book</h2>\n')
        file.writelines(f'\t\t<table border="1" width="600">\n')
        file.writelines(f'\t\t\t<thead>\n')
        file.writelines(f'\t\t\t<tbody>\n')
        file.writelines(f'\t\t\t\t<tr>\n')
        file.writelines(f'\t\t\t\t\t<th>№</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Фамилия</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Имя</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Телефон</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Комментарий</th>\n')
        file.writelines(f'\t\t\t\t</tr>\n')
        file.writelines(f'\t\t\t</thead>\n')
        count = 1
        for text in arr:
            file.writelines(f'\t\t\t\t<tr>\n')
            file.writelines(f'\t\t\t\t\t<td>{count}</td> \n')
            for item in text:
                file.writelines(f'\t\t\t\t\t<td>{item}</td> \n')
            file.writelines(f'\t\t\t\t</tr>\n')
            count += 1
        file.writelines(f'\t\t\t</tbody>\n')
        file.writelines(f'\t\t</table>\n')
        file.writelines(f'\t</body>\n')
        file.writelines(f'</html>')
