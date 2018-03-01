import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot, update):
	print(update)
	bottext="""Привет, {}!
Я бот Даши и понимаю простые команды. Для начала - команду {}""".format(update.message.chat.first_name, '/start')
	logging.info('Пользователь {} нажал команду /start'.format(update.message.chat.username))
	update.message.reply_text(bottext)

def chat(bot, update):
	text=update.message.text
	logging.info(text)
	update.message.reply_text(text)

def main():
	updtr=Updater(settings.TELEGRAM_API_BOT_KEY)

	updtr.dispatcher.add_handler(CommandHandler("Start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))


	updtr.start_polling()
	updtr.idle()

if __name__=="__main__":
	logging.info("Bot started")
	main()
