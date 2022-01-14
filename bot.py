import logging
from xmlrpc.client import Boolean
import aiogram
from aiogram import Bot, Dispatcher, executor, types
import sqlite3
from db import Database
import keyboard


  
logging.basicConfig(level=logging.INFO)




bot = Bot(token='bots API', parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)

db = Database('database.db')



def user_exist(id):

	if(db.user_exists(id)):

		return True

	else:

		return False

# реакция на запуск бота
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	isAuthorized = user_exist(message.from_user.id)

	if isAuthorized == False:

		await bot.send_message(message.from_user.id, "Пожалуйста введите ваше имя, фамилия и должность")

		if(len(message.text) > 60):

			await bot.send_message(message.from_user.id, "Ваше имя, фамилия, а так же отдел и должность не должны превышать 60 символов")
			
		else:

			db.set_nickname(message.from_user.id, message.text)
			db.set_signup(message.from_user.id, "done")
			await bot.send_message(message.from_user.id, "Регистрация прошла успешно!")
			isAuthorized=True

	elif isAuthorized == True:

		await bot.send_message(message.from_user.id, "Вы уже зарегестрированны")

	elif message.text == 'Профиль':

		user_nickname = 'Ваши данные: ' + db.get_nickname(message.from_user.id)
		await bot.send_message(message.from_user.id, user_nickname)

	elif message.text == 'Создать Заявку':

		await message.reply("Пожалуйста опишите вашу проблему и в начале строки поставьте символ @")
	if '@' in message.text:
		name = message.from_user.first_name
		surname = message.from_user.last_name  
		msg = f'Завяка от {name} {surname}: {message.text} '
		
		# ТУТ ДОЛЖНА БЫТЬ СРОЧНОСТЬ

		# Отправляем заявку админу
		await bot.send_message(1077163964, msg)
		db.set_message(message.from_user.id, message.text)
	

		# это я не трогал
    # реакция на нажатие кнопки
@dp.callback_query_handler(lambda c: c.data)
async def btns_reactions(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
    
    if call.data == 'very_fast':
        # Отправляем срочность заявки админу

        # save priority to bd
        msg = f'Заявка от {call.message.from_user.first_name} {call.message.from_user.last_name} \n\n {text_mess} высокой срочности'
        await bot.send_message(1077163966, msg)

    elif call.data == 'medium_fast':
        # Отправляем срочность заявки админу

        # save priority to bd
            # найти пользователя в бд по user_id == message.from_user.id
            # установить приоритет
        msg = f'Заявка от {call.message.from_user.first_name} {call.message.from_user.last_name} \n\n {text_mess} средней срочности'
        await bot.send_message(1077163966, msg)


#58572335 id sergey

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)