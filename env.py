def openenv():
    return open("env", "r")

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
