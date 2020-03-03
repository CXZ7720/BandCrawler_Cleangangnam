import re


def parseAddress(content):
    # @TODO : 정규표현식 개선필요.
    # p = re.compile(
        # '(((대치|삼성) ?(\d*?)? ?동) ?((\d*)? ?(-?) ?(\d*)?(번지)?))|(([가-힣]*(길|로)).(\d*.)?(길|로)?.(\d*).(\d*))|(고려.?.?)')
    p = re.compile('(대치로 ?(\d{0,5})?)|(삼성로 ?(\d{0,5})?길?)|(봉은사로 ?(\d{0,5})?)|(선릉로 ?(\d{0,5})?길?)|(학동로 ?(\d{0,5})?길?)|(도곡로 ?(\d{0,5})?길?)|(영동대로 ?(\d{0,5})길?)|(역삼로 ?(\d{0,5})?길?)|(테헤란로 ?(\d{0,5})?길?)|(.고려.)')
    q = re.compile('(성진)|(상록수)|(웅비)|(하진)|(하남)|(로얄)|(태화)|(평원)')# 예외조건
    reg_res = p.search(content)
    except_res = q.search(content)
    if reg_res:
        m = reg_res.group()
        if except_res: # 예외조건에 해당하는 경우 None 리턴
            print("Not our business!!")
            return None
        # print(m)
        return m
    else:
        return None

def companyAuthor(author):
    q = re.compile('(성진)|(상록수)|(웅비)|(하진)|(하남)|(로얄)|(태화)|(평원)|(동환특수)')# 예외조건
    result = q.search(author)

    if result:
        print("Not our business : Author - " + result.group())
        return False # 다른 업체에서 올린경우 처리 false
    else:
        return True