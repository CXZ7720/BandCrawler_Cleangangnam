import os

def openenv():
    try:
        return open(os.getcwd()+"/BandCrawler_Cleangangnam/env", "r") #Crontab 실행환경
    except:
        return open(os.getcwd() + "/env", "r") # 개발환경

def getenv(file):
    env = {}
    lines = file.readlines() # 줄별로 읽어서 배열로 리턴

    # for Github Actions
    env['band_token'] = os.getenv('band_token')
    env['db_usr'] = os.getenv('db_user')
    env['db_pwd'] = os.getenv('db_pwd')
    env['db_name'] = os.getenv('db_name')
    env['telegram_token'] = os.getenv('telegram_token')
    env['channel_id'] = os.getenv('channel_id')

    if None in env.values():
        print("OS env not fund. Using local file value")
        env['band_token'] = lines[0][:-1]
        env['db_usr'] = lines[1][:-1]
        env['db_pwd'] = lines[2][:-1]
        env['db_name'] = lines[3][:-1]
        env['telegram_token'] = lines[4][:-1]
        env['channel_id'] = lines[5]

    return env

