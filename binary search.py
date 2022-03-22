import random
a = [random.randint(0, 50000) for i in range(0, 20)]
#a = [i for i in range(0, 50)]

a.sort()

def search(b, val):
    i = len(b) // 2
    if b[i] == val:
        return i
    elif b[i] < val:
        return i + search(b[i:], val)
    elif b[i] > val:
        return search(b[:i], val)

print(a)
print(a[15])
print(search(a, a[15]))