import sys

n = list(map(int, sys.stdin.readline().strip().split()))

sys.stdout.write(str(abs(sum(n[::2]) - sum(n[1::2]))))