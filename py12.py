list1 = [[4,1], [3,2], [2,3], 4]
def decode(List):
    def step(List1):
        if isinstance(List1, list):
            return [(List1[1], range(List1[0]))]
        else:
            return [(List1, [0])]
    return [x for List1 in List for x, R in step(List1) for i in R]
print(decode(list1))
