import logging
from telegram import Update
import subprocess
import livescore
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

score_data = livescore.get_live_matches()

API_KEY ='7330939999:AAE3m3exRTB9MGsTsk1jK1foIRZOMISk79E'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello Welcome T20 Cricket Score Bot!")


async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    script_path = "livescore.py"
    subprocess.call(["python", script_path])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=score_data)


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_KEY).build()
    
    start_handler = CommandHandler('start', start)
    score_handler = CommandHandler('score', score)
    application.add_handler(start_handler)
    application.add_handler(score_handler)
    
    application.run_polling()