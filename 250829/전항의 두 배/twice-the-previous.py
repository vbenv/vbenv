n = list(map(int, input().split()))
print(n[0], n[1], end=' ')
for i in range(8):
    n.append(2*n[i] + n[i+1])
    print(n[-1], end = ' ')
