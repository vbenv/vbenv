import sys
n = list(map(int, sys.stdin.readline().strip().split()))\
for i in range(1,10):
    if n[i] % 3 == 0:
        sys.stdout.write(n[i-1])
        break