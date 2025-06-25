from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, URLInputFile
from aiogram.types import URLInputFile
#from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import image, folder
from filters.filters import IsAdmin, IsFolder
from keyboards.keyboards import folders_kb, foto_keyboard

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart(), IsAdmin())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start']) #Вывожу клавиатуру
    #await message.answer(image())
    #await message.answer(text=str(folder()))
    #await message.answer_photo(photo=image())
    #print(message.from_user.id)

@router.message(Command(commands='folder'), IsAdmin())
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/folder'], reply_markup=folders_kb(folder())) #Вывожу клавиатуру

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'), IsAdmin())
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

@router.message(IsFolder(list(folder())), IsAdmin())
async def process_help_command(message: Message):
    #await message.answer(text='Это папка')
    global fold_name
    fold_name=message.text
    await message.answer_photo(photo=image(f'/bot/{message.text}'), reply_markup=foto_keyboard)

@router.callback_query(F.data == 'next')
async def process_button_1_press(callback: CallbackQuery):
    #URL = ''
    #print(callback.message.photo)
    #while URL == callback.message.photo:
    #    URL = image('/bot/ДР_Славы')
    #    print(URL)
    URL = image(f'/bot/{fold_name}')
    print(fold_name)
    await callback.message.edit_media(
        media=InputMediaPhoto(
            #media='https://i.pinimg.com/originals/13/43/01/134301657fd893e65ff2c4f29c4ba74c.jpg'
            media=str(URL)
        ),
        #reply_markup=list(folders_kb(folder()))
        reply_markup=foto_keyboard
    )

@router.callback_query(F.data == 'fold_b')
async def process_button_1_press(message: Message):
    #URL = ''
    #print(callback.message.photo)
    #while URL == callback.message.photo:
    #    URL = image('/bot/ДР_Славы')
    #    print(URL)
    await message.answer(text='Выберите нужную папку', reply_markup=folders_kb(folder())) #Вывожу клавиатуру