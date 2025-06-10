from telegram.ext import ApplicationBuilder, CommandHandler
import os

BOT_TOKEN = os.environ.get("7914441896:AAEyZ3xf2BG7pC-ST_joHWPNbxNVT1muifU")

async def start(update, context):
    await update.message.reply_text("הבוט פעיל 🎉 שלח לי קישור!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
