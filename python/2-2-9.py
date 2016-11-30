def count():
    fs=[]
    for i in range(1, 4):
        def f(j):
            def k():
                return j * j
            return k
        r=f(i)
        fs.append(r)
    return fs
f1,f2,f3=count()
print f1()
print f2()
print f3()
print f1.__name__