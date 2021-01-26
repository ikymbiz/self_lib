#!/usr/bin/python
# -*- coding: utf-8 -*-
"""tr_text
> .dic_val(word, dictionary)

> .dic_key(word, dictionary)

> .zen_han(word)

> .tr_areas(address)

> .tr_company(companyName)

Todo:


"""

import re

def dic_val(word, dictionary):
    """dic_val(word, dictionary)

    If the part of word is in dictionary key,
    replace 'word' to dictionary 'value'.

    Args:
        word (obj): Word to be replaced
        dictionary (dict): dictionary{key:value}

    Returns:
       obj: Replaced word by value

    Examples:

    Note:

    """
    for key, value in dictionary.items():
        if key in word:
            ret = value
            break
        else:
            ret = "False"
    return ret

def dic_key(word, dictionary):
    """dic_key(word, dictionary)

    If the part of word is in dictionary key,
    replace 'word' to dictionary 'key'.

    Args:
        word (obj): Word to be replaced
        dictionary (dict): dictionary{key:value}

    Returns:
       obj: Replaced word by key

    Examples:

    Note:

    """
    for key, value in dictionary.items():
        if value in word:
            ret = key
            break
        else:
            ret = "False"
    return ret


def zen_han(word):
    """zen_han(word)
    全角から半角に変換する
    """
    tbl_zen2han = str.maketrans({"１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9","０":"0",
                 "ア":"ｱ","イ":"ｲ","ウ":"ｳ","エ":"ｴ","オ":"ｵ",
                 "カ":"ｶ","キ":"ｷ","ク":"ｸ","ケ":"ｹ","コ":"ｺ",
                 "サ":"ｻ","シ":"ｼ","ス":"ｽ","セ":"ｾ","ソ":"ｿ",
                 "タ":"ﾀ","チ":"ﾁ","ツ":"ﾂ","テ":"ﾃ","ト":"ﾄ",
                 "ナ":"ﾅ","ニ":"ﾆ","ヌ":"ﾇ","ネ":"ﾈ","ノ":"ﾉ",
                 "ハ":"ﾊ","ヒ":"ﾋ","フ":"ﾌ","ヘ":"ﾍ","ホ":"ﾎ",
                 "マ":"ﾏ","ミ":"ﾐ","ム":"ﾑ","メ":"ﾒ","モ":"ﾓ",
                 "ヤ":"ﾔ","ユ":"ﾕ","ヨ":"ﾖ",
                 "ラ":"ﾗ","リ":"ﾘ","ル":"ﾙ","レ":"ﾚ","ロ":"ﾛ",
                 "ワ":"ﾜ","ヲ":"ｦ","ン":"ﾝ",
                 "Ａ":"A","Ｂ":"B","Ｃ":"C","Ｄ":"D","Ｅ":"E","Ｆ":"F","Ｇ":"G",
                 "Ｈ":"H","Ｉ":"I","Ｊ":"J","Ｋ":"K","Ｌ":"L","Ｍ":"M","Ｎ":"N",
                 "Ｏ":"O","Ｐ":"P","Ｑ":"Q","Ｒ":"R","Ｓ":"S","Ｔ":"T","Ｕ":"U",
                 "Ｖ":"V","Ｗ":"W","Ｘ":"X","Ｙ":"Y","Ｚ":"Z",
                 "ａ":"a","ｂ":"b","ｃ":"c","ｄ":"d","ｅ":"e","ｆ":"f","ｇ":"g",
                 "ｈ":"h","ｉ":"i","ｊ":"j","ｋ":"k","ｌ":"l","ｍ":"m","ｎ":"n",
                 "ｏ":"o","ｐ":"p","ｑ":"q","ｒ":"r","ｓ":"s","ｔ":"t","ｕ":"u",
                 "ｖ":"v","ｗ":"w","ｘ":"x","ｙ":"y","ｚ":"z",
                 "！":"!","％":"%","（":"(","）":")","＝":"=","ー":"-","＾":"^",
                 "～":"~","｜":"|","、":",","＜":"<","。":".","＞":">",
                 "；":";","：":":","＋":"+","＊":"*",
                 "＠":"@","‘":"`","［":"[","］":"]","？":"?","＿":"_"})
    return word.translate(tbl_zen2han)


def tr_areas(address):
    """tr_areas(address)
        tr_areas: replace 丁目/番地/番/号
    """
    tbl_areas = {"丁目":"-","番地":"-","番":"-","号":";"}
    return re.sub('({})'.format('|'.join(map(re.escape, tbl_areas.keys()))), lambda m: tbl_areas[m.group()], self)

def tr_company(companyName):
    tbl_company = {"株式会社":"株","(株)":"(株)"}
    return re.sub('({})'.format('|'.join(map(re.escape, tbl_company.keys()))), lambda m: tbl_company[m.group()], self)

