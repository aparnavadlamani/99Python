list = [1,2,3,2,1]
def palindrome(list):
    return list == list[::-1]
print(palindrome(list))
