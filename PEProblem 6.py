lst = []
n = 0
while n <= 100:
    n1 = n**2
    lst.append(n1)
    n += 1

def lstsum(lst):
    sum = 0
    i = 0
    while i < len(lst):
        sum += lst[i]
        i += 1
    return sum

a = lstsum(lst)
print(a)

lst2 = []
n = 0
while n <= 100:
    lst2.append(n)
    n += 1

b = (lstsum(lst2)) ** 2
print(b)

print(b-a)