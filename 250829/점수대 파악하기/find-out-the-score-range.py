n = list(map(int, input().split()))
tmp = [0]* 10
for i in n:
    if i == 0:
        break
    tmp[(i//10)-1] += 1
for idx in range(9,-1,-1):
    print(f"{(idx+1)*10} - {tmp[idx]}")