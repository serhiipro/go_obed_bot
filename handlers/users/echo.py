from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.poll_states import PollStates
from copy import deepcopy
from aiogram.utils.markdown import hlink

from loader import dp, bot
from utils.misc.places import places_dict


@dp.message_handler(text='/get_menus')
async def send_i_will_poll(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = get_menus_list(data if data else places_dict)
    await message.answer('Ссылки на меню \n\n' + text)


@dp.message_handler(text='/go_obed')
async def send_i_will_poll(message: types.Message):
    await bot.send_poll(message.chat.id, question='Го обед?', options=['го', 'не го'])


@dp.message_handler(text='/popular_poll')
async def choose_place(message: types.Message):
    options = get_places_name_list(places_dict)
    await bot.send_poll(message.chat.id, question='Куда?', options=options)


@dp.message_handler(text='/add_option')
async def add_optionl(message: types.Message):
    await message.answer('Введите ваш вариант заведения')
    await PollStates.GetOptionState.set()


@dp.message_handler(state=PollStates.GetOptionState)
async def add_option_to_poll(message: types.Message, state: FSMContext):
    custom_option = message.text
    await state.update_data(custom_option=custom_option)
    await message.answer(
        'Введите ссылку на меню предложенного заведения. (или не вводите, это ваша жизнь живите её. Введите "ну лан")')
    await PollStates.GetOptionLinkState.set()


@dp.message_handler(state=PollStates.GetOptionLinkState)
async def add_link_for_option(message: types.Message, state: FSMContext):
    custom_option = await state.get_data()
    data = deepcopy(places_dict)
    data['addditional_place'] = {'name': custom_option.get('custom_option'),
                                 'link': message.text if 'http' in message.text else ''}
    await state.reset_state()
    await state.update_data(data=data)
    data = await state.get_data()
    options = get_places_name_list(data)
    await bot.send_poll(message.chat.id, question='Куда?', options=options)


def get_menus_list(data=None):
    return '\n\n'.join([hlink(data.get(key).get('name'), data.get(key).get('link')) for key in data])


def get_places_name_list(places=None):
    return [places.get(key).get('name') for key in places]
