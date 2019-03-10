list1 = ['a','b','c','d','e','f','g','h','i','j']
n = int(input())
print([x for i, x in enumerate(list1) if (i+1)%n])
