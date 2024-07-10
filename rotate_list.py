def reverse(lst , k):
    k = k % len(lst)
    rotate = lst[-k : ] + lst[ : -k]
    return rotate

list = [1,2,3,4,5]
i = 7
print(reverse(list,i))