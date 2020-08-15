TOKEN = 'TELEGRAM BOT TOKEN'
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from fill_invites import main as invite_main
from send_email import send_email
import threading
from validate_email import validate_email


def message(update, context):
    text = update.message.text
    if validate_email(text):
        update.message.reply_text('כתובת אימייל התקבלה.')
        update.message.reply_text('אנא המתן לקבלת ההזמנה. תהליך זה יכול לקחת כמה דקות')
        send_email(text)
        update.message.reply_text('הזמנה נשלחה בהצלחה! \n שים לב שאם ההזמנה לא התקבלה - כנראה הזנת כתובת אימייל לא נכונה, אתה כבר רשום, או שאולי ההזמנה הגיעה לפח האשפה.')
        update.message.reply_text('על מנת להרחיב את הקהילה עוד יותר, נשמח אם תוכל לבקש מחברים ואנשים שבעניין להירשם גם כן! \n t.me/FuzerInviteBot')

    
    else:
        update.message.reply_text('אנא הזן כתובת אימייל תקנית על מנת לקבל הזמנה. אם אתה לא יודע מה לעשות - הקלד /start')

def start(update, context):
    """Send a message when the command /start is issued."""
    string = """ברוך הבא לבוט ההזמנות של fuzer!
הבוט פותח על ידי משתמש FXP: The_beat.

על מנת לקבל הזמנה - הזן את כתובת האימייל שלך (מומלצת כתובת אימייל של ג'ימייל), ותקבל הזמנה תוך מספר דקות. 
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
