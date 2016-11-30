def log(f):
    def fn(*args, **kw):
        print 'calling %s' %(f.__name__)
        return f(*args, **kw)
    return fn
@log 
def fac():
    sum = 1
    for i in range(1,10):
        sum *= i
    return sum
print fac()
