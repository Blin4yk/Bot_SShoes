from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Define the keyboard for main menu
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
main_keyboard.add(
    KeyboardButton(text="Категория"),
    KeyboardButton(text="Описание"),
    KeyboardButton(text="FAQ")
)

# Define the keyboard for catigories menu
categories_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
categories_keyboard.add(
    KeyboardButton(text="Сезон"),
    KeyboardButton(text="Тип обуви"),
    KeyboardButton(text="Материал")
)

# Define the keyboard for season menu
season_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
season_keyboard.add(
    KeyboardButton(text="Лето"),
    KeyboardButton(text="Зима"),
    KeyboardButton(text="Весна"),
    KeyboardButton(text="Осень")
)

# Define the keyboard for FAQ
faq_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
faq_keyboard.add(
    KeyboardButton(text="Заказ"),
    KeyboardButton(text="Доставка"),
    KeyboardButton(text="Реквизиты"),
    KeyboardButton(text="Вся информация")
)

# Define the keyboard for the type shoes
type_shoes_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
type_shoes_keyboard.add(
    KeyboardButton(text="Кроссовки"),
    KeyboardButton(text="Кеды"),
    KeyboardButton(text="Ботинки"),
    KeyboardButton(text="Тапки")
)