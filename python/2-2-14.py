import functools
def cmp_ignore_case(x,y):
    return cmp(x.upper(),y.upper())
new_sort = functools.partial(sorted,cmp = cmp_ignore_case)
print new_sort(['adam','Zeal','DECK'])