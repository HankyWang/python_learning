def prod(lst):
    def result():
        sum = 1
        for i in lst:
            sum *= i
        return sum
    return result
lst = [1,2,3,4,5,6,7,8,9,10]
f = prod(lst)
print f()
print f.__name__
print f