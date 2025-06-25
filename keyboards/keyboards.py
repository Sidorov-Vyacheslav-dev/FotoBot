from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

def folders_kb(folders):
    #kb_build = ReplyKeyboardBuilder()
    kb_build = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=str(i)) for i in list(folders)
    ]
    kb_build.row(*buttons, width=3)
    keyboard: ReplyKeyboardMarkup = kb_build.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(text='Назад к папкам', callback_data='fold_b')
#big_button_2 = InlineKeyboardButton(text='👎', callback_data='big_button_2_pressed') 👍
big_button_3 = InlineKeyboardButton(text='Следующие фото', callback_data='next')


# Создаем объект инлайн-клавиатуры
foto_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_3]]
)