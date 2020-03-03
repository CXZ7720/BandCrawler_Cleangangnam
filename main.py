import bandCrawler as bc
import parseAddress as parse
import db
import bot
import re


def main():
    band_ID = bc.getBandInfo()
    band_Post = bc.getBandPost(band_ID, bc.band_token)

    parsed_data = []
    for i in band_Post['result_data']['items']:
        temp = bc.makeData(i)  # 1개의 처리 데이터를 임시로 딕셔너리 형태로 저장.
        postkey = temp.get('postkey')
        createdate = temp.get('createdate')
        photos = temp.get('photos')

        # Postkey 로 DB를 조회하여 새로운 게시글인지 확인하여 글 개수를 리턴(새글 : 0, 이미 등록된 글 : 1)
        isExist = db.search_postkey(postkey)  # 0 || 1
        if (isExist == 1):  # 이미 등록된 글이면
            print("Already exists : " + postkey)
            continue
        else:  # 새글일 경우
            print("Add to DB")
            db.insertPost(postkey, createdate)
            print("본문내용 : " + temp['content'])
            parsed_address = parse.parseAddress(temp['content'])  # 정규표현식에 의한 주소 파싱(str)
            print("주소파싱 결과 : " + str(parsed_address))
            findAuthor = parse.companyAuthor(temp['author'])
            if (parsed_address != None and findAuthor == True):
                print("파싱결과 - 고려환경 민원 확인!")
                text = """<b>새로운 민원이 등록되었습니다!</b>\n<b>찾은 단어 : %s</b>\n\n<b>작성자 :</b> %s\n<b>등록일 :</b> %s\n<b>내용 :</b> \n%s\n""" \
                       % (parsed_address, temp['author'], temp['createdate'], temp['content'])
                bot.sendMessage(text)
                print(photos)
                if len(photos) > 0:
                    try :
                        bot.sendImage(photos)
                    except:
                        print("Timeout")
                db.afterSend(postkey)

main()
