from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.texts import BotText

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BotText.get_data),
            KeyboardButton(text=BotText.collect_data),
        ],
        [
            KeyboardButton(text=BotText.subscription_activation),
            KeyboardButton(text=BotText.subscription_deactivation),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...',
)
cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=BotText.cancel)]],
    resize_keyboard=True,
    one_time_keyboard=True,
)
