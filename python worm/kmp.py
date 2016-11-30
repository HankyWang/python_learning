def get_next(mode):
    j = 0
    k = -1
    m = len(mode)
    next = [0 for i in range(m)]
    next[0] = -1
    while j < m-1:
        if k==-1 or mode[j]==mode[k]:
            j+=1
            k+=1
            if (mode[j] == mode[k]):
                next[j] = next[k]
            else:
                next[j] = k
        else:
            k = next[k]
    return next

def match(str,mode):
    m = len(mode)
    n = len(str)
    i = 0
    j = 0
    next = get_next(mode)
    while (j<m and i<n):
        if j == -1 or mode[j]==str[i]:
            j += 1
            i += 1
        else:
            j = next[j]
    if j == m:
        return i - j
    else:
        return -1

str = 'abbbc'
mode = 'bbb'
ans = match(str,mode)
print ans