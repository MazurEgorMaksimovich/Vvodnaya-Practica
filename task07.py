n = int(input())
for i in range(1, n+1):
    y = 0
    for _ in range(-2, n-i):
        print(y, end=' ')
        y+=1
    print()