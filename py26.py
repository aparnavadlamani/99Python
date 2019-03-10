from itertools import combinations
list1 = [1,2,3,4,5]
n = int(input())
list2 = list(combinations(list1,n))
print(list2)
