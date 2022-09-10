n = int(input())
y = 0
for i in range(1, n+1):
    for _ in range(-1, n-i):
        print(n-y, end=' ')
    y += 1
    print()