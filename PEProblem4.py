def palindrome(n: int) -> bool:
    nstring = str(n)
    nstringlst = list(nstring)
    nstring2 = []
    j = -1
    while j >= (-len(nstringlst)):
        nstring2.append(nstringlst[j])
        j -= 1
    i= 0
    while i < len(nstringlst):
        if nstringlst[i] != nstring2[i]:
            return False
        else:
            pass
        i += 1
    return True



lst = []
for n1 in range(100, 999):
    for n2 in range(100, 999):
        product = n1 * n2
        if palindrome(product):
            lst.append(product)

print(max(lst))

