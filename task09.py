n = int(input())
l = 1
i = 1
while i <= n:
    s = ''
    k = -1
    for _ in range(l):
        k += 1
        if i > n:
            s = (' ' * (len(str(i))+1)*(l-k)  + s)
            break
        s = (str(i) + ' ' + s)
        i += 1
    print(s)
    l += 1