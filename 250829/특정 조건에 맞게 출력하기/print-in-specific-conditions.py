n = list(map(int, input().split()))
for i in range(len(n)):
    if n[i] == 0:
        for _ in range(i):
            if n[_] % 2 == 0:
                print(n[_]//2, end = ' ')
            else:
                print(n[_] + 3, end = ' ')
        break    