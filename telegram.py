import telebot
import env

env_file = env.openenv()
env_vars = env.getenv(env_file)

bot = telebot.TeleBot(env_vars['telegram_token'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "안녕하세요! 강남구청 청소업체 Band 새글알림 봇이에요.")



def sendMessage(text):
    cid = 658295242
    bot.send_message(cid, text)


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot.set_update_listener(listener)  # register listener

# bot.polling()