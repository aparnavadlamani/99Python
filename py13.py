list1 = [1,1,1,1,1,2,2,2,2,3,3,3]
from itertools import groupby
def encode(List):
    def modfy(a,listy):
        l = len(list(listy))
        if l>1:
            return [l, a]
        else:
            return a
    return [modfy(a,group) for a, group in groupby(List)]
print(encode(list1))
