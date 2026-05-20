import random
import string
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8975254524:AAE6M-Hxz1r29z8tjEg5plpbbkI4u7PVghE"

CHANNEL_USERNAME = "@D_ARK_COM"

app = ApplicationBuilder().token(TOKEN).build()


async def check_join(user_id, bot):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            return True

        return False

    except:
        return False


def generate_username():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(5))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    joined = await check_join(user_id, context.bot)

    if not joined:
        await update.message.reply_text(
            """
لازم تشترك في القناة أولًا ❌

https://t.me/D_ARK_COM

بعد الاشتراك ارسل /start
"""
        )
        return

    await update.message.reply_text(
        """
أهلا بك ✅

الأوامر:
/gen - توليد يوزرات
"""
    )


async def gen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    joined = await check_join(user_id, context.bot)

    if not joined:
        await update.message.reply_text(
            "اشترك بالقناة أولًا ❌"
        )
        return

    usernames = []

    for _ in range(20):
        username = generate_username()
        usernames.append(f"@{username}")

    result = "\n".join(usernames)

    await update.message.reply_text(
        f"يوزرات مقترحة:\n\n{result}"
    )


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gen", gen))

print("Bot Started ✅")

app.run_polling()