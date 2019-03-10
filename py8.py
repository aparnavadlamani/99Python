list1 = [1,1,1,2,2,2,2,3,3,3,3,3]
from itertools import groupby
print([x[0] for x in groupby(list1)])
