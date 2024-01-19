def ovl(lon):
    sum = 0
    for n in lon:
        sum += n
    return sum



first = 1
second = 2
lon = [second]
while True:
     fibonacci = first + second
     first = second
     second = fibonacci
     if fibonacci > 4000000:
         break
     if fibonacci%2 == 0:
         lon.append(fibonacci)


print(ovl(lon))

