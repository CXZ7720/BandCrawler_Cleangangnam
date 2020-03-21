import os


def getenv():
    env = {
        'band_token': os.getenv('band_token'),
        'db_usr': os.getenv('db_usr'),
        'db_pwd': os.getenv('db_pwd'),
        'db_name': os.getenv('db_name'),
        'telegram_token': os.getenv('telegram_token'),
        'channel_id': os.getenv('channel_id')
    }

    return env
