import os

def openenv():
    try:
        return open(os.getcwd()+"/BandCrawler_Cleangangnam/env", "r") #Crontab 실행환경
    except:
        return open(os.getcwd() + "/env", "r") # 개발환경

def getenv(file):
    env = {}
    lines = file.readlines() # 줄별로 읽어서 배열로 리턴
    env['band_token'] = lines[0][:-1]
    env['db_usr'] = lines[1][:-1]
    env['db_pwd'] = lines[2][:-1]
    env['db_name'] = lines[3][:-1]
    env['telegram_token'] = lines[4][:-1]
    env['channel_id'] = lines[5]

    return env
