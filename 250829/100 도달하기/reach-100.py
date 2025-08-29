n = int(input())
nn = 1
sum = 0
print(nn, n, end = ' ')
while n <= 100:
    nn, n = n, nn+n
    print(n, end = ' ')