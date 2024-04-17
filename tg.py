import telebot
from telebot import types

token = '6499786748:AAHtLB3jwOlk9PiFAkbQvs9cDMxB1JVN_Yo'
my_chat_id = 6465719518
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b1 = types.KeyboardButton(text='Услуги')
    b2 = types.KeyboardButton(text='О нас')
    b3 = types.KeyboardButton(text='Оставить заявку')
    keyboard.add(b1, b2, b3)
    bot.send_message(message.chat.id, 'Здраствуйте! Мы бухгалтерская компания! Добро Пожаловать❤️', reply_markup=keyboard)


def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Ссылка на наш сайт', url='https://reallyworld.ru')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Информация о нас👍', reply_markup=keyboard)


def send_request(message):
    mes = f'Новая заявка:{message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо за заявку! Наши специлаисты скоро с вами свяжуться😊💕!')


def send_service(message):
    bot.send_message(message.chat.id, '1. Составить годовой отчет')
    bot.send_message(message.chat.id, '2. Оплатить налоги')
    bot.send_message(message.chat.id, '3. Расчитать бюджет')


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'о нас':
        info_func(message)
    if message.text.lower() == 'оставить заявку':
        bot.send_message(message.chat.id, 'Будем рады вас обслужить! Оставьте свой контактный данные!😁')
        bot.register_next_step_handler(message, send_request)
    if message.text.lower() == 'услуги':
        send_service(message)


if __name__ == '__main__':
    bot.infinity_polling()
