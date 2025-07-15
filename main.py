import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("הבוט באוויר ✅ תן פקודה")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("סטטוס: תקין. אני מקשיב לך אח!")
async def daily_tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 טיפ יומי: נוסח מומלץ לשלוח ליריב:\n\n"
        "1. מכבי ת״א – ניצחון\n"
        "2. צ׳לסי – תיקו\n"
        "3. קורינתיאנס – הפסד\n\n"
        "(נוסח דוגמה, נעדכן לפי תחזיות אמח)"
    )


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("סטטוס", status))
app.add_handler(CommandHandler("טופס", daily_tip))

app.run_polling()
