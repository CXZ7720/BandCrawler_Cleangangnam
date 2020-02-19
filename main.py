import bandCrawler as bc
import parseAddress as parse
import db
import bot


def main():
    band_ID = bc.getBandInfo()
    band_Post = bc.getBandPost(band_ID, bc.band_token)

    parsed_data = []
    for i in band_Post['result_data']['items']:
        temp = bc.makeData(i)  # 1개의 처리 데이터를 임시로 딕셔너리 형태로 저장.
        postkey = temp.get('postkey')
        createdate = temp.get('createdate')

        # Postkey 로 DB를 조회하여 새로운 게시글인지 확인하여 글 개수를 리턴(새글 : 0, 이미 등록된 글 : 1)
        isExist = db.search_postkey(postkey)  # 0 || 1
        if (isExist == 1):  # 이미 등록된 글이면
            print("Already exists")
            continue
        else:  # 새글일 경우
            print("Add to DB")
            db.insertPost(postkey, createdate)
            print("본문내용 : " + temp['content'])
            parsed_address = parse.parseAddress(temp['content'])  # 정규표현식에 의한 주소 파싱(str)
            print("주소파싱 결과 : " + str(parsed_address))
            if (parsed_address != None):
                print("파싱결과 - 고려환경 민원 확인!")
                text = "<b>새로운 민원이 등록되었습니다!</b><br>" \
                       "작성자 : %s<br>" \
                       "등록일 : %s<br>" \
                       "내용 : <br>%s<br>" % (temp['author'], temp['createdate'], temp['content'])
                bot.sendMessage(text)
                db.afterSend()
            # @TODO parsed_address를 이용한 kakao locla API 검색
            # @TODO 검색 결과를 카카오톡 API를 이용하여 전송
            # @TODO 전송 완료후 DB 1로 업데이트


main()
