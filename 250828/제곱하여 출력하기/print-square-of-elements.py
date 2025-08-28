import sys
c = sys.stdin.readline()
n = list(map(int, sys.stdin.readline().strip().split()))


[sys.stdout.write(str( i ** 2 ) + ' ') for i in n]