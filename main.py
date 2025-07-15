import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("הבוט באוויר ✅ תן פקודה")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("סטטוס: תקין. אני מקשיב לך אח!")

async def daily_tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 טופס מומלץ יומי:
1. מכבי ת"א - ניצחון
2. צ'לסי - תיקו
3. קורינתיאנס - הפסד

(סתם דוגמה, נעדכן לפי תחזיות אמת)")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("סטטוס", status))
app.add_handler(CommandHandler("טופס", daily_tip))

app.run_polling()
