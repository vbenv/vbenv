n = int(input())
cnt = 0
t = 1
while True:
    mul = n*t
    print(mul, end = ' ')
    t += 1
    if mul % 5 == 0:
        cnt += 1

    if cnt == 2:
        break