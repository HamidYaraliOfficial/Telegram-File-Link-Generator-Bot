import telebot
import requests
import time

# Created by: https://github.com/HamidYaraliOfficial
# Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==

TOKEN = "Token_here"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "سلام! فایل، عکس یا ویدیوی خود را بفرستید تا لینک دانلود آن تولید شود\n"
        "Hello! Send your file, photo, or video to generate a download link\n"
        "Привет! Отправь файл, фото или видео, чтобы создать ссылку для скачивания\n"
        "你好！发送你的文件、照片或视频以生成下载链接", 
        parse_mode="Markdown")

@bot.message_handler(content_types=['document', 'photo', 'video'])
def handle_file(message):
    file_id = None
    if message.document:
        file_id = message.document.file_id
    elif message.photo:
        file_id = message.photo[-1].file_id  # آخرین عکس (با کیفیت بالا)
    elif message.video:
        file_id = message.video.file_id
    if file_id:
        # Send the initial 'creating link' message
        msg = bot.reply_to(message, 
            "❖ **Creating the link**...\n"
            "❖ **Создание ссылки**...\n"
            "❖ **正在创建链接**...", 
            parse_mode="Markdown")
        # Get file information from Telegram
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
        # Shorten the Telegram file URL using TinyURL
        api_url = f"https://tinyurl.com/api-create.php?url={file_url}"
        response = requests.get(api_url)
        if response.status_code == 200 and response.text.startswith("https://tinyurl.com/"):
            short_url = response.text
            # Edit the message with the bold link
            bot.edit_message_text(
                f"**❖ The link is ready\n❖ Link:**\n`{short_url}`\n"
                f"**❖ Ссылка готова\n❖ Ссылка:**\n`{short_url}`\n"
                f"**❖ 链接已准备好\n❖ 链接:**\n`{short_url}`",
                chat_id=message.chat.id, 
                message_id=msg.message_id, 
                parse_mode="Markdown")
        else:
            bot.edit_message_text(
                "❌ Error in shortening the URL. Please try again.\n"
                "❌ Ошибка при сокращении URL. Пожалуйста, попробуйте снова.\n"
                "❌ 缩短URL时出错。请重试。",
                chat_id=message.chat.id, 
                message_id=msg.message_id, 
                parse_mode="Markdown")
    else:
        bot.reply_to(message, 
            "⚠️ لطفاً یک فایل معتبر ارسال کنید!\n"
            "⚠️ Please send a valid file!\n"
            "⚠️ Пожалуйста, отправьте действительный файл!\n"
            "⚠️ 请发送有效文件！", 
            parse_mode="Markdown")

bot.polling(non_stop=True)