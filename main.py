import telebot

# 🔑 توكن البوت من BotFather
API_TOKEN = '8077784427:AAFXM_QfoC_i-TEeowgAlRjwdrRm78YpWVc'
bot = telebot.TeleBot(API_TOKEN)

# 🎬 قاعدة بيانات بسيطة للمسلسلات والحلقات
series_data = {
    "الحافظ الحامي": [
        {"title": "الحلقة 1", "url": "https://example.com/hafiz1.mp4"},
        {"title": "الحلقة 2", "url": "https://example.com/hafiz2.mp4"}
    ],
    "حلم أشرف": [
        {"title": "الحلقة 1", "url": "https://example.com/ashraf1.mp4"}
    ]
}

# ✅ رسالة الترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
        "👋 أهلاً بك في بوت المسلسلات\n\n"
        "📺 أرسل اسم المسلسل لعرض الحلقات المتاحة."
    )

# 📥 استقبال اسم المسلسل وعرض حلقاته
@bot.message_handler(func=lambda message: True)
def show_episodes(message):
    user_text = message.text.strip()
    
    if user_text in series_data:
        episodes = series_data[user_text]
        reply = f"📺 الحلقات المتوفرة لمسلسل *{user_text}*:\n\n"
        for ep in episodes:
            reply += f"🎞️ {ep['title']}\n📎 {ep['url']}\n\n"
        bot.send_message(message.chat.id, reply, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "❌ لم أجد هذا المسلسل.\n📌 حاول كتابة الاسم بشكل صحيح.")

# 🚀 تشغيل البوت
bot.polling(non_stop=True)
