import collections

def flatten(l):
    '''listを平坦化する\
    agg: list[]\
    \
    2次元のリストを平坦化 : itertools.chain.from_iterable()\
    \
    https://note.nkmk.me/python-list-flatten/
    
    '''
    for el in l:
        if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el