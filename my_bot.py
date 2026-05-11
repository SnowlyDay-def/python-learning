import telebot

bot = telebot.TeleBot("TOKEN")

bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Сап! Я твой бот. Напиши мне 'hell' или 'god damn'!")

@bot.message_handler(func=lambda message: True)
def handle_all_text(message):
    user_text = message.text.lower()

    if user_text == "hell" or user_text == "hall":
        bot.send_message(message.chat.id, "WTH R U SAYING NAHHH")
    elif user_text == "god damn":
        bot.send_message(message.chat.id, "oo god damn okey")
    else:
        bot.send_message(message.chat.id, f"Sorry, у мя пока нет команды '{message.text}'")

    bot.infinity_polling()
