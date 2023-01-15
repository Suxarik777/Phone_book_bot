from telebot import TeleBot, types
import emoji


# ReplyKeyboard
def but_start_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    but_1 = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
    markup.add(but_1)
    return markup

def but_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    but_1 = types.KeyboardButton(emoji.emojize(':eyes: Посмотреть данные'))
    but_2 = types.KeyboardButton(emoji.emojize(':writing_hand: Ввести данные'))
    but_3 = types.KeyboardButton(emoji.emojize(':backhand_index_pointing_right: Редактировать'))
    but_4 = types.KeyboardButton(emoji.emojize(':card_index_dividers: Экспорт в файл'))
    markup.add(but_1, but_2, but_3, but_4)
    return markup



# InlineKeyboad
def but_inline_init():
    markup = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(emoji.emojize(':keyboard: с клавиатуры'),
                                       callback_data='с клавиатуры')
    but_2 = types.InlineKeyboardButton(emoji.emojize(':file_folder: из файла'),
                                       callback_data='из файла')
    markup.add(but_1, but_2)
    return markup

def but_inline_format_file():
    markup = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(emoji.emojize(':triangular_ruler: .csv'),
                                       callback_data='csv')
    but_2 = types.InlineKeyboardButton(emoji.emojize(':spider_web: .html'),
                                       callback_data='html')
    markup.add(but_1, but_2)
    return markup


def but_inline_view():
    markup = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(emoji.emojize(':person_tipping_hand: по номеру записи'),
                                       callback_data='номер записи')
    but_2 = types.InlineKeyboardButton(emoji.emojize(':man_detective: искать'),
                                       callback_data='искать')
    but_3 = types.InlineKeyboardButton(emoji.emojize(':family_man_woman_girl_boy: смотреть всех'),
                                       callback_data='смотреть всех')
    markup.add(but_1, but_2, but_3)
    return markup


def but_inline_edit_two_step():
    markup = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(emoji.emojize(':wastebasket: удалить'),
                                       callback_data='удалить')
    but_2 = types.InlineKeyboardButton(emoji.emojize(':pen: редактировать'),
                                       callback_data='редактировать')
    markup.add(but_1, but_2)
    return markup

def but_inline_export():
    markup = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(emoji.emojize(':triangular_ruler: .csv'),
                                       callback_data='csv_export')
    but_2 = types.InlineKeyboardButton(emoji.emojize(':spider_web: .html'),
                                       callback_data='html_export')
    but_3 = types.InlineKeyboardButton(emoji.emojize(':cross_mark_button: .xml'),
                                       callback_data='xml_export')
    markup.add(but_1, but_2, but_3)
    return markup

# def but_inline_return():
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     but_1 = types.InlineKeyboardButton(emoji.emojize(':BACK_arrow: вернутся назад'),
#                                        callback_data='вернутся назад')
#     markup.add(but_1)
#     return markup
