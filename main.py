from telegram import Update
from telegram.ext import Application , ContextTypes , filters , CommandHandler , MessageHandler;

# بخش مورد نظر اینه که بهتره این فایل های توکن ما و یوزر ما در یک فایل ای ان وی جدا قرار گرفته بشه برای امنیت بیشتر و درنهایت در این قسمت ایمپورت بشه
TOKEN = "8291008854:AAGFaTBT229PiGcQpzk3_BFOfEb8ttlmn_U"
BOT_USERNAME = "@amingholipourbot"

# مدیریت کامل دکمه هایی که میشود ساخت 
async def start_command(update : Update , context : ContextTypes.DEFAULT_TYPE ):
    user = update.effective_user
    await update.message.reply_text(f'Hi!{user or ''} welcome to the amin-style-code')
    
async def help_command(update : Update , context : ContextTypes.DEFAULT_TYPE ):
    
        await update.message.reply_text(f'im a simple bot you used me at  /help , /start , /coustom ')

async def custom_command(update : Update , context : ContextTypes.DEFAULT_TYPE ):
    
        await update.message.reply_text(f'im a private bot')
