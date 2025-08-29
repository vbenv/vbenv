import sys
nn,n = map(int, sys.stdin.readline().strip().split())

print(nn, n, end = ' ')
for _ in range(8):
    nn, n = n, n+nn
    if n >= 10:
        n -= 10
    print(abs(n), end = ' ')
    