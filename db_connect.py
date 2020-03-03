import pymysql
import env

env_file = env.openenv()
env_vars = env.getenv(env_file)
# print(env_vars['db_usr'])
# print(env_vars['db_pwd'])
# print(env_vars['db_name'])


conn = pymysql.connect(host='cxz7720.gonetis.com', port=13306, user=env_vars['db_usr'], passwd=env_vars['db_pwd'], db=str(env_vars['db_name']), charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)