# Telegram File Link Generator Bot

## English

### Overview
This project is a Telegram bot designed to generate shortened download links for files, photos, or videos sent by users. Built using Python and the `python-telegram-bot` library, the bot leverages the Telegram API to retrieve file information and the TinyURL API to create shortened URLs. It provides a simple and efficient way for users to share downloadable content directly through Telegram.

### Features
- **File Handling**: Accepts documents, photos, and videos sent via Telegram.
- **Link Generation**: Creates shortened download links using the TinyURL API for easy sharing.
- **Multilingual Support**: Interacts with users in English, Persian, and Chinese.
- **User-Friendly Feedback**: Provides clear status messages during link creation, including success and error notifications.
- **High-Quality Image Support**: Automatically selects the highest quality photo when multiple sizes are available.

### Prerequisites
- Python 3.6 or higher.
- Required Python libraries: `python-telegram-bot` and `requests`.
- A valid Telegram bot token obtained from BotFather.
- An active internet connection to interact with the Telegram and TinyURL APIs.

### Setup
1. Install the required Python libraries:
   ```bash
   pip install python-telegram-bot requests
   ```
2. Update the `TOKEN` variable in the `bot.py` script with your Telegram bot token.
3. Run the script on a server or local machine with internet access:
   ```bash
   python bot.py
   ```
4. Start interacting with the bot by sending the `/start` command in Telegram.

### Usage
1. Send the `/start` command to the bot to receive a welcome message.
2. Send a file, photo, or video to the bot.
3. The bot will respond with a message indicating that it is creating the link.
4. Once processed, the bot will provide a shortened TinyURL link for downloading the file, or an error message if the process fails.

### Notes
- Ensure the bot token is kept secure and not shared publicly.
- The bot handles only one file at a time and requires valid file types (documents, photos, or videos).
- The TinyURL API is used for shortening links, which may have rate limits or require an API key for heavy usage.
- Created by: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)
- Instagram: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)

---

## فارسی

### مرور کلی
این پروژه یک ربات تلگرامی است که برای تولید لینک‌های کوتاه‌شده دانلود برای فایل‌ها، عکس‌ها یا ویدیوهای ارسالی توسط کاربران طراحی شده است. این ربات با استفاده از پایتون و کتابخانه `python-telegram-bot` ساخته شده و از API تلگرام برای دریافت اطلاعات فایل و API TinyURL برای ایجاد URLهای کوتاه‌شده استفاده می‌کند. این ربات راهی ساده و کارآمد برای اشتراک‌گذاری محتوای قابل دانلود از طریق تلگرام ارائه می‌دهد.

### ویژگی‌ها
- **مدیریت فایل‌ها**: پذیرش اسناد، عکس‌ها و ویدیوهای ارسالی از طریق تلگرام.
- **تولید لینک**: ایجاد لینک‌های دانلود کوتاه‌شده با استفاده از API TinyURL برای اشتراک‌گذاری آسان.
- **پشتیبانی چندزبانه**: تعامل با کاربران به زبان‌های انگلیسی، فارسی و چینی.
- **بازخورد کاربرپسند**: ارائه پیام‌های وضعیت واضح در طول فرآیند تولید لینک، شامل اعلان‌های موفقیت و خطا.
- **پشتیبانی از تصاویر با کیفیت بالا**: انتخاب خودکار عکس با بالاترین کیفیت در صورت وجود چندین اندازه.

### پیش‌نیازها
- پایتون نسخه 3.6 یا بالاتر.
- کتابخانه‌های پایتون مورد نیاز: `python-telegram-bot` و `requests`.
- توکن معتبر ربات تلگرامی که از BotFather دریافت شده است.
- اتصال فعال به اینترنت برای تعامل با APIهای تلگرام و TinyURL.

### راه‌اندازی
1. کتابخانه‌های مورد نیاز پایتون را نصب کنید:
   ```bash
   pip install python-telegram-bot requests
   ```
2. متغیر `TOKEN` را در اسکریپت `bot.py` با توکن ربات تلگرامی خود به‌روزرسانی کنید.
3. اسکریپت را روی یک سرور یا ماشین محلی با دسترسی به اینترنت اجرا کنید:
   ```bash
   python bot.py
   ```
4. با ارسال دستور `/start` در تلگرام، تعامل با ربات را آغاز کنید.

### استفاده
1. دستور `/start` را به ربات ارسال کنید تا پیام خوش‌آمدگویی دریافت کنید.
2. یک فایل، عکس یا ویدیو به ربات ارسال کنید.
3. ربات با پیامی پاسخ می‌دهد که نشان‌دهنده در حال ایجاد بودن لینک است.
4. پس از پردازش، ربات یک لینک کوتاه‌شده TinyURL برای دانلود فایل ارائه می‌دهد یا در صورت بروز خطا، پیام خطا نمایش می‌دهد.

### نکات
- اطمینان حاصل کنید که توکن ربات امن نگه داشته شده و به‌صورت عمومی به اشتراک گذاشته نشود.
- ربات تنها یک فایل را در هر زمان پردازش می‌کند و نیاز به انواع فایل معتبر (اسناد، عکس‌ها یا ویدیوها) دارد.
- API TinyURL برای کوتاه کردن لینک‌ها استفاده می‌شود که ممکن است محدودیت‌های نرخ داشته باشد یا برای استفاده سنگین نیاز به کلید API داشته باشد.
- ساخته شده توسط: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)
- اینستاگرام: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)

---

## 中文

### 概述
该项目是一个Telegram机器人，旨在为用户发送的文件、照片或视频生成短链接下载地址。该机器人使用Python和`python-telegram-bot`库构建，利用Telegram API获取文件信息，并通过TinyURL API创建短链接。它为用户提供了一种简单高效的方式，通过Telegram直接分享可下载内容。

### 功能
- **文件处理**：接受通过Telegram发送的文档、照片和视频。
- **链接生成**：使用TinyURL API创建短链接，便于分享。
- **多语言支持**：支持用英语、波斯语和中文与用户交互。
- **用户友好的反馈**：在链接生成过程中提供清晰的状态消息，包括成功和错误通知。
- **高质量图片支持**：当有多个尺寸的图片时，自动选择最高质量的图片。

### 前提条件
- Python 3.6或更高版本。
- 必需的Python库：`python-telegram-bot`和`requests`。
- 从BotFather获取的有效Telegram机器人令牌。
- 连接到互联网以与Telegram和TinyURL API交互。

### 设置
1. 安装所需的Python库：
   ```bash
   pip install python-telegram-bot requests
   ```
2. 在`bot.py`脚本中更新`TOKEN`变量为您的Telegram机器人令牌。
3. 在具有互联网访问权限的服务器或本地机器上运行脚本：
   ```bash
   python bot.py
   ```
4. 在Telegram中发送`/start`命令以开始与机器人交互。

### 使用方法
1. 向机器人发送`/start`命令以接收欢迎消息。
2. 向机器人发送文件、照片或视频。
3. 机器人将回复一条消息，表示正在创建链接。
4. 处理完成后，机器人将提供一个TinyURL短链接用于下载文件，或在发生错误时显示错误消息。

### 注意事项
- 确保机器人令牌安全且不公开分享。
- 机器人一次仅处理一个文件，且需要有效的文件类型（文档、照片或视频）。
- TinyURL API用于缩短链接，可能有速率限制或在高负载使用时需要API密钥。
- 作者：[HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)
- Instagram: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)