from telegram.ext import ApplicationBuilder, CommandHandler
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("הבוט פעיל 🎉 שלח לי קישור!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
