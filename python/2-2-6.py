from math import sqrt
def is_sqr(a):
    if sqrt(a) % 1 ==0:
        return 1
    else :
        return 0

print filter(is_sqr,range(1,101))