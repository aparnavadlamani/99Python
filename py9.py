list1 = [1,1,1,2,2,2,2,3,3,3,3,3]
from itertools import groupby
print([list(group) for x, group in groupby(list1)])
