N = int(input())

# 이전 줄만 저장 (슬라이딩 윈도우)
max_prev = [0, 0, 0]
min_prev = [0, 0, 0]

# 첫 번째 줄 입력받고 초기화
first_line = list(map(int, input().split()))
for i in range(3):
    max_prev[i] = first_line[i]
    min_prev[i] = first_line[i]

# 두 번째 줄부터 처리
for idx in range(1, N):
    cur_line = list(map(int, input().split()))
    max_cur = [0, 0, 0]
    min_cur = [0, 0, 0]

    for x in range(3):
        max_candidate = []
        min_candidate = []

        for j in range(-1, 2):
            if 0 <= x+j <= 2:
                max_candidate.append(max_prev[x+j])
                min_candidate.append(min_prev[x+j])

        max_cur[x] = max(max_candidate) + cur_line[x]
        min_cur[x] = min(min_candidate) + cur_line[x]

    # 현재 줄을 이전 줄로 업데이트
    max_prev = max_cur
    min_prev = min_cur

print(f"{max(max_prev)} {min(min_prev)}")


"""
3
1 2 3
4 5 6
4 9 0
"""