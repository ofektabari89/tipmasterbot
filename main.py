import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# טוען את משתני הסביבה מהקובץ .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# פקודת התחלה
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("הבוט באוויר ✅ תן פקודה")

# פקודת סטטוס
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("סטטוס: תקין. אני מקשיב לך אח!")

# פקודת טופס יומי
async def daily_tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """🎯 טיפ יומי (דוגמה):
1. מכבי ת״א – ניצחון
2. צ׳לסי – תיקו
3. קורינתיאנס – הפסד"""
    )

# בניית הבוט
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("סטטוס", status))
app.add_handler(CommandHandler("טופס", daily_tip))

# הרצת הבוט
if __name__ == "__main__":
    app.run_polling()
