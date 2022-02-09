import scriptbot as sc
import os 
from telegram import Update
from telegram.ext import CommandHandler,Updater,MessageHandler,Filters,CallbackContext, dispatcher
import logging 

# Enable logger 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN=os.environ.get("ACCESS_TOKEN")
PORT= int(os.environ.get('PORT', 5000))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def infos(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello ! My name is {context.bot.get_me().first_name}\nMy father is @Kily99 and my username is @{context.bot.get_me().username}")

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Code commands before using them boy ! Thanks !")

def generic(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stop doing stupid things bro ! ")

def week(update: Update, context=CallbackContext):
    try:
        emploi=sc.weekSchedule(context.args[0])
        print("Day request received 1")
    except:
        emploi=sc.weekSchedule()
        print("Day request received 2")

    resp='\n'.join(emploi)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{resp}")

def ceJour(update: Update, context=CallbackContext):
    try:
        emploi=sc.ceJour(context.args[0],context.args[1]) # Ajouter un parametre à la commande
    except:
        emploi=sc.ceJour(context.args[0])
    resp='\n'.join(emploi)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{resp}")  

def Jour(update: Update, context=CallbackContext):
    try:
        emploi=sc.jour(context.args[0])
        print("Day request received 1")
    except:
        emploi=sc.jour()
        print("Day request received 2")
    resp='\n'.join(emploi)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{resp}")  



def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    print("connected")

    # Adding commands
    week_handler=CommandHandler("week", week,pass_args=True) 
    dispatcher.add_handler(week_handler)

    ceJour_handler=CommandHandler("dday", ceJour,pass_args=True) 
    dispatcher.add_handler(ceJour_handler)

    jour_handler=CommandHandler("today", Jour,pass_args=True) 
    dispatcher.add_handler(jour_handler)

    dispatcher.add_error_handler(error)

    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)

    generic_handler = MessageHandler(Filters.text & (~Filters.command), generic)
    dispatcher.add_handler(generic_handler)

    info_handler= CommandHandler('info',infos)
    dispatcher.add_handler(info_handler)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('yourwebhook_url' + TOKEN)

    updater.idle()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
