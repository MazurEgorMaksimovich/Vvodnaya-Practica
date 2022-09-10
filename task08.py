n = int(input())
l = 1
i = 1
while i < n:
    for _ in range(l):
        print(i, end=' ')
        if i > n:
            break
        else:
            i +=1
    print()
    l += 2