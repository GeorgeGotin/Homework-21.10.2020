import time


def insertion_sort(a):
    size = len(a)
    for i in range(size):
        for j in range(i+1, size):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]
    return a


def buble_sort(a):
    size = len(a)
    for i in range(size):
        for j in range(i+1, size):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


def shake_sort(a):
    size = len(a)
    for i in range(size//2):
        for j in range(i+1, size-i-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
            if a[size-j] < a[size-j-1]:
                a[size-j], a[size-j-1] = a[size-j-1], a[size-j]
    return a


def shell_sort(a):
    size = len(a)
    for i in range(size//2):
        for j in range(size//2+i):
            if a[j] > a[j+size//2-i]:
                a[j], a[j+size//2-i] = a[j+size//2-i], a[j]
    return a


def merge_sort(a):
    size = len(a)
    if size > 2:
        part1 = merge_sort(a[:size//2])
        part2 = merge_sort(a[size//2:])
        size1, size2 = size//2, size-size//2
        a = []
        i, j = 0, 0
        while i < size1 and j < size2:
            if part1[i] < part2[j]:
                a.append(part1[i])
                i += 1
            else:
                a.append(part2[j])
                j += 1
        if i < size1:
            a.extend(part1[i:])
        else:
            a.extend(part2[j:])

    elif size > 1:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]

    return a


s = input()
numbers = s.split(',')
a = []
for c in numbers:
    if c == '' or c == ' ' or c == '\n':
        continue
    a.append(float(c))
print(*a)
start = time.time()
print(*insertion_sort(a), (time.time()-start))
start = time.time()
print(*buble_sort(a), (time.time()-start))
start = time.time()
print(*shake_sort(a), (time.time()-start))
start = time.time()
print(*merge_sort(a), (time.time()-start))
