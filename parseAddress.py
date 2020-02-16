import re


def parseAddress(content):

    p = re.compile(
        '(((대치|삼성) ?(\d*?)? ?동) ?((\d*)? ?(-?) ?(\d*)?(번지)?))|(([가-힣]*(길|로)).(\d*.)?(길|로)?.(\d*).(\d*))')  ## 지번주소 완성. 도로명주소 추가 필요.
    # ([가-힣]+ ?((\d{1,5})?) ?[가-힣]? ?(\d{1,5})? ?-? ?(\d{1,6})? ?)
    if p != str:
        return None
    m = p.match(content).group()

    return m
