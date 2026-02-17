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
        
# مدیریت پیام ها 
def handel_response(text=str):
    if not text:
        return "undefined!!"

    usertext = text.lower().strip()

    # سلام و احوالپرسی
    if "hi" in usertext or "سلام" in usertext:
        return "Hi dear! How can I help you?"

    if "how are you" in usertext or "حالت چطوره" in usertext:
        return "I'm fine. How about you?"

    if "im fine" in usertext or "خوبم" in usertext:
        return "I'm happy to hear that! 😊"

    # خداحافظی
    if "bye" in usertext or "خداحافظ" in usertext or "خدا نگهدار" in usertext:
        return "Goodbye! Have a nice day!"

    # تشکر
    if "thank you" in usertext or "مرسی" in usertext or "متشکرم" in usertext:
        return "You're welcome! 😄"

    # سوال درباره اسم
    if "your name" in usertext or "اسمت چیه" in usertext:
        return "I'm your friendly assistant! What's your name?"

    # احوالپرسی دوستانه
    if "what's up" in usertext or "چه خبر" in usertext:
        return "Not much, just here to help you! 😎"

    # پاسخ پیش‌فرض
    return "I'm sorry, I cannot understand your answer."
