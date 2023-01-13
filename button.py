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

# def but_inline_return():
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     but_1 = types.InlineKeyboardButton(emoji.emojize(':BACK_arrow: вернутся назад'),
#                                        callback_data='вернутся назад')
#     markup.add(but_1)
#     return markup
