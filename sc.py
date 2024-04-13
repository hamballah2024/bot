from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
import requests

# Fungsi untuk menangani perintah /maxstream
def maxstream_command(update, context):
    # Memeriksa apakah perintah memiliki argumen URL
    if len(context.args) > 0:
        # Mendapatkan URL dari argumen perintah
        url = context.args[0]
        # Memproses URL Maxstream
        processed_result = process_maxstream_url(url)
        reply_message = f"*MPD Maxstream :* {url}\n\n*PSSH Maxstream :* `{processed_result}`"
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_message, parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Silakan masukkan URL setelah perintah /maxstream.")

# Fungsi untuk menangani perintah /vision
def vision_command(update, context):
    # Memeriksa apakah perintah memiliki argumen URL
    if len(context.args) > 0:
        # Mendapatkan URL dari argumen perintah
        url = context.args[0]
        # Memproses URL Vision
        processed_result = process_vision_url(url)
        reply_message = f"*MPD Vision :* {url}\n\n*PSSH Vision :* `{processed_result}`"
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_message, parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Silakan masukkan URL setelah perintah /vision.")

# Fungsi untuk memproses URL Maxstream
def process_maxstream_url(url):
    processed_url = requests.get("https://cendolcen.my.id/tools/script/pssh-maxstream-bot/sc.php?mpd=" + url)
    return processed_url.text

# Fungsi untuk memproses URL Vision
def process_vision_url(url):
    processed_url = requests.get("https://cendolcen.my.id/tools/script/pssh-maxstream-bot/vision.php?mpd=" + url)
    return processed_url.text

def main():
    # Token bot Telegram Anda
    token = '7129313428:AAFP1ELIdIqJ37Sx94eDGHb35Vn5on26kW4'

    # Membuat objek updater dan dispatcher
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah /maxstream
    maxstream_handler = CommandHandler('maxstream', maxstream_command)
    dispatcher.add_handler(maxstream_handler)

    # Menambahkan handler untuk perintah /vision
    vision_handler = CommandHandler('vision', vision_command)
    dispatcher.add_handler(vision_handler)

    # Memulai polling untuk bot Anda
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()