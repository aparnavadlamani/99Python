list1 = [1,1,1,1,1,2,2,2,2,3,3,3,4]
from itertools import groupby
def encode(List):
    def modfy(List1):
        if len(List1)>1:
            return [len(List1), List1[0]]
        else:
            return List1[0]
    return [modfy(list(group)) for x, group in groupby(List)]
print(encode(list1))
