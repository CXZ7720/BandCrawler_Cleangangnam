import re


def parseAddress(content):

    p = re.compile(
        '(((대치|삼성) ?(\d*?)? ?동) ?((\d*)? ?(-?) ?(\d*)?(번지)?))|(([가-힣]*(길|로)).(\d*.)?(길|로)?.(\d*).(\d*))|(고려.?.?)')

    if p != str:
        return None
    m = p.match(content).group()

    return m
