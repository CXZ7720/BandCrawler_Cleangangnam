import env
import telegram


env_file = env.openenv()
env_vars = env.getenv(env_file)
telegram_token = env_vars['telegram_token']
channel_id = env_vars['channel_id']

bot = telegram.Bot(token = telegram_token)

# updates = bot.getUpdates()
# print(updates)
#
# for i in updates:
#     print(i)

# print('start telegram chat bot')

#ID : 658295242
def sendMessage(message):
    bot.sendMessage(chat_id = channel_id, text=message, parse_mode=telegram.ParseMode.HTML)

def sendImage(url):
    bot.send_photo(chat_id=channel_id, photo=url, disable_notification=True, timeout=30)