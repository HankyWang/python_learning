from math import sqrt
print filter(lambda x:1 if sqrt(x) % 1 == 0 else 0,range(1,101))