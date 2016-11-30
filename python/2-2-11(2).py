from time import time
def perfromance(f):
    def fn(*args ,**kw):
        t1 = time()
        r = f(*args, **kw)
        t2 = time()
        print 'call %s %fs spent' %(f.__name__,(t2 - t1))
        return r
    return fn
@perfromance
def fac(x):
    sum = 1
    for i in range(1, x + 1):
        sum *= i
    return sum
print fac(20)
print fac(10)