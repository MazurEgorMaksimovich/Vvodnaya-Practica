n = int(input())
for i in range(1, n+1):
    y = 0
    for _ in range(i):
        print(i-y, end=' ')
        y += 1
    print()