list1 = [[1,2],[3,4],[5,6,7],[8,9]]
def flattennestedlist(List):
    for item in List:
        if isinstance(item, list):
            for subitem in item:
                yield subitem
        else:
            yield item
flatlist = list(flattennestedlist(list1))
print(flatlist)
