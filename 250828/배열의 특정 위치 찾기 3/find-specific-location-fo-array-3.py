import sys

n =list(map(int, sys.stdin.readline().strip().split()))
for i in range(3, len(n)):
    if n[i] == 0:
        print(sum(n[i-3:i]))
        break