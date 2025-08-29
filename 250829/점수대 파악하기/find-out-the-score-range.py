n = list(map(int, input().split()))
tmp = [0]* 11
for i in n:
    if i == 0:
        break
    tmp[(i//10)] += 1
for idx in range(10,0,-1):
    print(f"{(idx)*10} - {tmp7[idx]}")