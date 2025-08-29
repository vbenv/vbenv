c = input()
n = list(map(int,input().split()))
[print(i, end=' ') for i in n if i%2==0]