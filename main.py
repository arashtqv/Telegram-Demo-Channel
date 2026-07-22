import telebot
import os
import logging
from dotenv import load_dotenv
load_dotenv()
warning_users = {}
Bad_words_list = [
    "کلمه بد 1",
    "کلمه بد 2",
    "کلمه بد 3",
    "کلمه بد 4",
    "کلمه بد 5",
    "کلمه بد 6",
    "کلمه بد 7",
    "کلمه بد 8",
    "کلمه بد 9",
    "کلمه بد 10",
    "کلمه بد 11",
    "کلمه بد 12",
    "کلمه بد 13",
    "کلمه بد 14",
    "کلمه بد 15",
    "کلمه بد 16",

]
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.chat_join_request_handler()
def accept(request):#قبول میکنه
    bot.approve_chat_join_request(request.chat.id,request.from_user.id)

@bot.message_handler(content_types=["new_chat_members"])
def khosh_amad_goii(message):
    bot.send_message(message.chat.id,f"hello dear {message.from_user.first_name}")


@bot.message_handler(commands=["pin"])
def pin(message):
    if message.reply_to_message:
        bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        bot.send_message(message.chat.id, f"پیام {message.reply_to_message.from_user.first_name} پین شد")
    else:
        bot.send_message(message.chat.id, "لطفا این دستور را به عنوان پاسخ به پیام کاربری که میخواهید پین کنید ارسال کنید.")
        
# ===================== PIN =====================

@bot.message_handler(commands=["kick"])
def kick(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        #در اینجا ایدی کاربر رو میگیریم که میخوایم کیک کنیم
        bot.kick_chat_member(message.chat.id, user_id)
        # در اینجا کاربر رو کیک میکنیم
        bot.send_message(message.chat.id, f"کاربر {message.reply_to_message.from_user.first_name} از گروه کیک شد")#اینجا از ریپلای مسیج استفاده کردیم که اسم کاربر کیک شده رو بگیریم و در پیام نشون بدیم
    else:
        bot.send_message(message.chat.id, "لطفا این دستور را به عنوان پاسخ به پیام کاربری که میخواهید کیک کنید ارسال کنید.")

# ===================== KICK =====================

@bot.message_handler(commands=["admin"])
def make_admin(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id#در اینجا ایدی کاربر رو میگیریم که میخوایم ادمین کنیم
        bot.promote_chat_member(
            message.chat.id,
            user_id,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_delete_stories=True

                                )#در اینجا کاربر رو ادمین میکنیم
        bot.send_message(message.chat.id, f"کاربر {message.reply_to_message.from_user.first_name} به عنوان ادمین افزوده شد")
    else:
        bot.send_message(message.chat.id, "لطفا این دستور را به عنوان پاسخ به پیام کاربری که میخواهید ادمین کنید ارسال کنید.")

@bot.message_handler(commands=["remove_admin"])
def remove_admin(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id#در اینجا ایدی کاربر رو میگیریم که میخوایم از ادمین برکنار کنیم
        bot.promote_chat_member(
            message.chat.id,
            user_id,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )#در اینجا کاربر رو از ادمینی برکنار میکنیم
        bot.send_message(message.chat.id, f"کاربر {message.reply_to_message.from_user.first_name} از ادمینی حذف شد")
    else:
        bot.send_message(message.chat.id, "لطفا این دستور را به عنوان پاسخ به پیام کاربری که میخواهید از  ادمینی برکنار کنید ارسال کنید.")

# ===================== ADMIN =====================

@bot.message_handler(commands=["ban"])
def ban(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id#در اینجا ایدی کاربر رو میگیریم که میخوایم بن کنیم
        bot.kick_chat_member(message.chat.id, user_id)#در اینجا کاربر رو بن میکنیم
        bot.send_message(message.chat.id, f"کاربر {message.reply_to_message.from_user.first_name} از گروه بن شد")
    else:
        bot.send_message(message.chat.id, "لطفا این دستور را به عنوان پاسخ به پیام کاربری که میخواهید بن کنید ارسال کنید.")
@bot.message_handler(commands=["unban"])
def unban(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id#در اینجا ایدی کاربر رو میگیریم که میخوایم از بن در بیاریم
        bot.unban_chat_member(message.chat.id, user_id)#در اینجا کاربر رو از بن در میاریم
        bot.send_message(message.chat.id, f"کاربر {message.reply_to_message.from_user.first_name} از بن در آمد")#اینجا نام کاربر رو از ریپلای میگیریم
    else:
        bot.send_message(message.chat.id, "لطفا این دستور را به عنوان پاسخ به پیام کاربری که میخواهید از بن در بیاورید ارسال کنید.")

# ===================== BAN =====================
def has_bad_word(message):
    for word in Bad_words_list:
        if word in message.text:
            return True
    return False

@bot.message_handler(func=lambda message: True)
def bad_word(message):
    # اگر کلمه ای از لیست کلمات بد در پیام بود اون پیام حذف میشه
    for word in Bad_words_list:
        if word in message.text:
            bot.delete_message(message.chat.id, message.message_id)
            break
    # اگر کاربر بالای چند دفعه از کلمات بد استفاده کنه از گرو کیک میشه
    # اگر این کاربر قبلا اخطار گرفته بود این شرط اجرا میشه و اخطارش یکی اضافه میشه
    if (
        str(message.from_user.id) in warning_users
    ):  # چرا اینجا str گذاشتیم چون دیکشنری فقط میتونه رشته بگیره و ایدی کاربر عدد هست و باید استر بشه
        warning_users[str(message.from_user.id)] += 1
        bot.send_message(
            message.chat.id,
            f"اخطار {warning_users[str(message.from_user.id)]} : لطفا از کلمات بد استفاده نکنید",
        )
    # اگر این کاربر قبلا اخطار نگرفته بود این شرط اجرا میشه و اخطارش یکی میشه
    else:
        warning_users[str(message.from_user.id)] = 1
        bot.send_message(
            message.chat.id,
            f"اخطار {warning_users[str(message.from_user.id)]} : لطفا از کلمات بد استفاده نکنید",
        )
    # اگر کاربر بالای 3 بار از کلمات بد استفاده کنه از گرو کیک میشه و اخطارش پاک میشه
    if warning_users[str(message.from_user.id)] >= 3:
        bot.send_message(
            message.chat.id,
            f"کاربر {message.from_user.first_name} به دلیل استفاده از کلمات بد از گروه کیک شد",
        )
        bot.kick_chat_member(message.chat.id, message.from_user.id)
        del warning_users[str(message.from_user.id)]
    return

bot.infinity_polling()
