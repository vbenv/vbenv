n = list(map(int, input().split()))
counts = [0] * 11 # 10점 단위 점수대 (10~19, 20~29, ..., 90~99)와 100점을 위한 배열

for score in n:
    if score == 0:
        break
    if 10 <= score <= 99:
        index = score // 10
        counts[index] += 1
    elif score == 100:
        counts[10] += 1

# 출력
for i in range(10, 0, -1):
    print(f"{i*10} - {counts[i]}")