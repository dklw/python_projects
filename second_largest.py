def sec(n):
    s = float('-inf')
    f = float('-inf')
    
    for i in n:
        if i > f:
            s = f
            f = i
        elif f > i > s:
            s = i
    return s
            
numbers = [1,2,45,76,99,69]
print(sec(numbers))
            