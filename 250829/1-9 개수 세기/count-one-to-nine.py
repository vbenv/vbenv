t = input()
n = list(map(int, input().split()))

for i in range(1, 10):
    cnt = 0
    for elm in n:
        if elm == i:
            cnt += 1
    print(cnt)