
import telegram

bot = telegram.Bot(token='110060299:AAE5ieuss9qWYXJtCI0OoEVZxy3XT1Jtwws')
print bot.getMe()

rc = bot.setWebhook('https://kinnernet-bot.appspot.com')
print 'setWebhook rc: '% rc

# updates = bot.getUpdates()




# for update in updates: 
# 	print update.message.text
# 	bot.sendMessage(chat_id=update.message.chat_id, text="I'm sorry Dave I'm afraid I can't do that.\n" +  update.message.text)



# print [u.message.text for u in updates]


# chat_id = bot.getUpdates()[-1].message.chat_id

# bot.sendMessage(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")