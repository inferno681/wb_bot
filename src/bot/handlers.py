from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from bot.keyboards import cancel_kb, main_kb
from bot.service import service
from bot.texts import BotText

router = Router()


class CollectData(StatesGroup):
    article = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Cmd start handler."""
    await message.answer(BotText.cmd_start_text_first)
    await message.answer(
        BotText.cmd_start_text_second,
        reply_markup=main_kb,
    )


@router.message(F.text.in_(BotText.buttons))
async def ask_article(message: Message, state: FSMContext):
    """Ask article handler."""
    await state.set_state(CollectData.article)
    await state.update_data({'message': message.text})
    await message.reply(BotText.ask_article, reply_markup=cancel_kb)


@router.message(CollectData.article)
async def handle_article(message: Message, state: FSMContext):
    """Article processing."""
    last_message = (await state.get_data()).get('message')

    if message.text == BotText.cancel:
        await cancel_handler(message, state)

    if message.text and message.text.isdigit():
        article = int(message.text)
    else:
        await message.answer(BotText.article_isdigit_message)
        return

    match last_message:
        case BotText.get_data:
            result = await service.get_product(article)
        case BotText.collect_data:
            result = await service.collect_data(article)
        case BotText.subscription_activation:
            result = await service.sub_activation(article)
        case BotText.subscription_deactivation:
            result = await service.sub_deactivation(article)
        case _:
            result = BotText.unknown_action

    await message.answer(result, reply_markup=main_kb)
    await state.clear()


@router.message(F.text == BotText.cancel)
async def cancel_handler(message: Message, state: FSMContext):
    """Cancel handler."""
    await state.clear()
    await message.answer(BotText.cancel_text, reply_markup=main_kb)
