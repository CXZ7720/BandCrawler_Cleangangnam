import re


def parseAddress(content):

    # p = re.compile(
        # '(((대치|삼성) ?(\d*?)? ?동) ?((\d*)? ?(-?) ?(\d*)?(번지)?))|(([가-힣]*(길|로)).(\d*.)?(길|로)?.(\d*).(\d*))|(고려.?.?)')
    p = re.compile('(.대치.)|(.삼성.)|(.고려.)')
    reg_res = p.search(content)
    if reg_res:
        m = reg_res.group()
        print(m)
        return m
    else:
        return None
