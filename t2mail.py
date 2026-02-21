import logging
from uuid import uuid4

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

from telegram.ext import InlineQueryHandler

from mailer import Mailer
from config import mail_sender, mail_password

tmailer = Mailer(mail_sender, mail_password)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm email bot, talk to me!")


async def send_mail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    email_data = ''.join(context.args)
    recepients = [email_data.split('|')[0].split('R:')[1]]
    subject = email_data.split('|')[1].split('S:')[1]
    content = email_data.split('|')[2].split('C:')[1]
    email_dict = {
        'subject':subject,
        'body':content
    }
    send_status = tmailer.send_mail(recepients, email_dict)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(send_status))
    
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I did not understand that command.")
    
    
if __name__ == '__main__':
    application = ApplicationBuilder().token('8435463488:AAEDIPwW0V-MKLzexG0M8JeWUnqLb_eIDVI').build()


    # run the fuction start  every time bot receives the command /start
    start_handler = CommandHandler('start', start)
    # turn text to caps with /caps command


    send_mail_handler = CommandHandler('send_mail', send_mail)
    
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    

    handlers = [
                start_handler,
                send_mail_handler,
                unknown_handler]

    for handler in handlers:
        application.add_handler(handler)



    application.run_polling()
