
"""Refference of of repl_text

"""

def dic_val(word, dictionary):
    for key, value in dictionary.items():
        if key in word:
            ret = value
            break
        else:
            ret = "False"
    return ret

def dic_key(word, dictionary):
    for key, value in dictionary.items():
        if value in word:
            ret = key
            break
        else:
            ret = "False"
    return ret