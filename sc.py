from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
import requests

# Fungsi untuk menangani perintah /maxstream
def maxstream_command(update, context):
    if len(context.args) > 0:
        url = context.args[0]
        
        # Menunjukkan bahwa bot sedang memproses permintaan
        context.bot.send_message(chat_id=update.message.chat_id, text="Sedang memproses...", reply_to_message_id=update.message.message_id)
        
        processed_result = process_maxstream_url(url)
        reply_message = f"*MPD Maxstream :* {url}\n\n*PSSH Maxstream :* `{processed_result}`"
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_message, parse_mode=ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Silakan masukkan URL setelah perintah /maxstream.", reply_to_message_id=update.message.message_id)

# Fungsi untuk menangani perintah /vision
def vision_command(update, context):
    if len(context.args) > 0:
        url = context.args[0]
        
        # Menunjukkan bahwa bot sedang memproses permintaan
        context.bot.send_message(chat_id=update.message.chat_id, text="Sedang memproses...", reply_to_message_id=update.message.message_id)
        
        processed_result = process_vision_url(url)
        reply_message = f"MPD Vision : {url}\n\nPSSH Vision : `{processed_result}`"
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_message, reply_to_message_id=update.message.message_id)

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Silakan masukkan URL setelah perintah /vision.", reply_to_message_id=update.message.message_id)

# Fungsi untuk menangani perintah /getmpdcubmu
def getmpdcubmu_command(update, context):
    if len(context.args) > 1:
        option = context.args[0]
        value = context.args[1]
        
        # Menunjukkan bahwa bot sedang memproses permintaan
        context.bot.send_message(chat_id=update.message.chat_id, text="Sedang memproses...", reply_to_message_id=update.message.message_id)

        processed_result = process_get_mpd(option, value)
        context.bot.send_message(chat_id=update.message.chat_id, text=processed_result, parse_mode=ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Silakan masukkan opsi (name atau id) dan nilai setelah perintah /getmpdcubmu.", reply_to_message_id=update.message.message_id)

# Fungsi untuk memproses URL Maxstream
def process_maxstream_url(url):
    processed_url = requests.get("https://cendolcen.my.id/tools/script/pssh-maxstream-bot/sc.php?mpd=" + url)
    return processed_url.text

# Fungsi untuk memproses URL Vision
def process_vision_url(url):
    processed_url = requests.get("https://cendolcen.my.id/tools/script/pssh-maxstream-bot/vision.php?mpd=" + url)
    return processed_url.text

# Fungsi untuk memproses MPD submu
def process_get_mpd(option, value):
    if option == 'name':
        processed_url = requests.get(f"https://cendolcen.my.id/tools/script/pssh-maxstream-bot/cari-cubmu-channel.php?name={value}")
    elif option == 'id':
        processed_url = requests.get(f"https://cendolcen.my.id/tools/script/pssh-maxstream-bot/cari-cubmu-channel.php?id={value}")
    else:
        return "Opsi tidak valid."
    
    data = processed_url.json()  # Mengubah respons ke format JSON
    if 'ID' in data:
        formatted_result = (
            f"ID: {data['ID']}\n"
            f"Nama: {data['Name']}\n"
            f"Kategori: {data['SubName']}\n"
            f"MPD URL: {data['IP']}\n"
            f"Image URL: {data['Image URL']}"
        )
        return formatted_result
    else:
        return "Data tidak ditemukan atau format respons salah."

def main():
    token = '7129313428:AAFP1ELIdIqJ37Sx94eDGHb35Vn5on26kW4'

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    maxstream_handler = CommandHandler('maxstream', maxstream_command)
    dispatcher.add_handler(maxstream_handler)

    vision_handler = CommandHandler('vision', vision_command)
    dispatcher.add_handler(vision_handler)

    getmpdcubmu_handler = CommandHandler('getmpdcubmu', getmpdcubmu_command)
    dispatcher.add_handler(getmpdcubmu_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
