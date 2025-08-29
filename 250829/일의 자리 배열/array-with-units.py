import sys
nn,n = map(int, sys.stdin.readline().strip().split())

sys.stdout.write(str(nn)+ ' ')
sys.stdout.write(str(n)+ ' ')
for _ in range(8):
    nn, n = n, ((n+nn) % 10)
    sys.stdout.write(str(n)+ ' ')
    