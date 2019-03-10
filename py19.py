list1 = [1,2,3,4,5]
n = int(input())
list2 = list1[n:]
list2.extend(list1[:n])
print(list2)
