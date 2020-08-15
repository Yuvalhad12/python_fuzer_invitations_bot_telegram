TOKEN = 'TELEGRAM BOT TOKEN'
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from fill_invites import main as invite_main
from send_email import send_email
import threading
from validate_email import validate_email


def message(update, context):
    text = update.message.text
    if validate_email(text):
        update.message.reply_text('EMAIL ADDRESS RECIEVED')
        update.message.reply_text('PLEASE WAIT FOR AN INVITATION. THE PROCESS CAN TAKE A FEW MINUTES')
        send_email(text)
        update.message.reply_text('INVITATION WAS SENT SUCCESSFULLY. NOTE THAT IF YOU HAVENT RECIEVED THE INVITATION, YOU EITHER PUT THE WRONG ADRRESS, ALREADY REGISTERED TO THE WEBSITE, OR THE EMAIL IS IN YOUR SPAM FOLDER')

    
    else:
        update.message.reply_text('PLEASE PUT AN EMAIL ADDRESS. IF YOU NEED HELP, TYPE /start')

def start(update, context):
    """Send a message when the command /start is issued."""
    string = """LONG INTRODUCTION BLA BLA
BLA BLA
"""
    update.message.reply_text(string)



def main():
    print('telegram_bot is activated')
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()
    print('bot is up and running')
    updater.idle()


t = threading.Thread(target= invite_main)
t.start()
main()
