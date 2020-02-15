import re


def parseAddress(content):
    p = re.compile('(((대치|삼성) ?(\d{1,3}?)? ?동) ?((\d{1,5})? ?(-?) ?(\d{1,4})?(번지)?))|()') ## 지번주소 완성. 도로명주소 추가 필요.
# ([가-힣]+ ?((\d{1,5})?) ?[가-힣]? ?(\d{1,5})? ?-? ?(\d{1,6})? ?)

    m = p.match(content).group()

    return m