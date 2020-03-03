import env
import telegram


env_file = env.openenv()
env_vars = env.getenv(env_file)
telegram_token = env_vars['telegram_token']
channel_id = env_vars['channel_id']

bot = telegram.Bot(token = telegram_token)


#ID : 658295242
def sendMessage(message):
    bot.sendMessage(chat_id = channel_id, text=message, parse_mode=telegram.ParseMode.HTML)

def sendImage(url):
    InputMediaPhotoObjList = []
    print(url)
    for i in range(len(url)):
        print(url[i])
        InputMediaPhotoObjList.append(telegram.InputMediaPhoto(url[i]))
    bot.sendMediaGroup(chat_id=channel_id, media=InputMediaPhotoObjList, disable_notification=True, timeout=30)
    # bot.send_photo(chat_id=channel_id, photo=url, disable_notification=True, timeout=30)