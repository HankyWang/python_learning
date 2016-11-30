from time import time
def performance(unit):
    def decorator(f):
        def wrapper(*args, **kw):
            t1 = time()
            r = f(*args, **kw)
            t2 = time()
            print 'call %s %f%s spent' %(f.__name__, (t2 - t1)*1000 if unit == 'ms' else (t2 - t1), unit)
            return r
        return wrapper
    return decorator
@performance('ms')
def fac(x):
    return reduce(lambda x,y:x * y, range(1, x+1))
print fac(20)