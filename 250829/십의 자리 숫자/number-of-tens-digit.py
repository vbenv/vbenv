n = list(map(int,input().split()))

for i in range(1,10):
    cnt = 0
    for elm in n:
        if elm == 0:
            break
        if int(elm*0.1) == i:
            cnt += 1
    print(f"{i} - {cnt}")