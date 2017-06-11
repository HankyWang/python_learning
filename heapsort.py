n = 10
def parent(i):
    return i // 2
def left(i):
    return i * 2
def right(i):
    return i * 2 + 1
def max_heapify(lst, i):
    global n
    l, r = left(i), right(i)
    if (l < n and lst[l] > lst[i]):
        maxx = l
    else :
        maxx = i
    if (r < n and lst[r] > lst[maxx]):
        maxx = r
    if (maxx != i):
        lst[maxx], lst[i] = lst[i], lst[maxx]
        max_heapify(lst, maxx)
def build_heap(lst):
    global n
    for i in range(n // 2, -1, -1):
        max_heapify(lst, i)

def heap_sort(lst):
    global n
    build_heap(lst)
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        n -= 1
        max_heapify(lst,0)

lst = [12,5,90,4,58,89,2,45,8,10]
heap_sort(lst)
print lst