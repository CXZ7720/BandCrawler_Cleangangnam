import urllib.request
import urllib.parse
import env
import json
from datetime import datetime

env_file = env.openenv()
env_vars = env.getenv(env_file)
print(env_vars['band_token'])

band_token = env_vars['band_token']




def getBandInfo():
    band_list_url = "https://openapi.band.us/v2.1/bands?access_token=" + band_token
    list_req = urllib.request.Request(band_list_url)
    list_res = urllib.request.urlopen(list_req)
    # band_key = "AAAf6yBsiOQlfYjGduGIh75v" 3kim band
    decoded_list = list_res.read().decode("utf8")
    # print(decoded_list)
    bandlist_json = json.loads(decoded_list)
    # print(bandlist_json)
    target_id = bandlist_json['result_data']['bands'][0]['band_key']
    # print(target_id)

    return target_id


def getBandPost(target_id, band_token):
    post_list_url = "https://openapi.band.us/v2/band/posts?access_token=" + band_token + "&band_key=" + target_id + "&locale=ko_KR"
    post_req = urllib.request.Request(post_list_url)
    post_res = urllib.request.urlopen(post_req)

    decoded_post = post_res.read().decode("utf8")
    # print(decoded_post)
    postlist_json = json.loads(decoded_post)

    # print(postlist_json)

    return postlist_json


def makeData(postlist_json):
    # for i in postlist_json['result_data']['items']:
    # print(i)
    author = postlist_json['author']['name']
    postkey = postlist_json['post_key']
    content = postlist_json['content']
    createdate = mil_to_date(postlist_json['created_at'])  # milisecond, long
    # print(i['photos'])
    photos = str(getPhotoUrl(postlist_json['photos']))  # 사진의 url이 담긴 배열을 리턴
    # print("========================================")

    # print("작성자 : " + author)
    # print("Post Key : " + postkey)
    # print("본문 : \n" + content)
    # print("작성일 : " + createdate)
    # print("사진 URL : " + str(photos))

    return {
        'author': author,
        'postkey': postkey,
        'content': content,
        'createdate': createdate,
        'photos': photos
    }


def getPhotoUrl(photo_array):
    # print(photo_array[0])
    res = []
    for key in photo_array:
        res.append(key.get('url'))
    if len(res) == 0:
        res.append("사진 없음")

    return res


def mil_to_date(milliseconds):
    return str(datetime.fromtimestamp(milliseconds // 1000))
