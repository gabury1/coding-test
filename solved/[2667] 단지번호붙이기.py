def dfs(y, x):
    if not (0 <= y < n and 0 <= x < n) or grid[y][x] == 0:
        return 0

    grid[y][x] = 0
    count = 1

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        count += dfs(y + dy, x + dx)

    return count


n = int(input())
grid = [list(map(int, input())) for _ in range(n)]

complexes = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            complexes.append(dfs(i, j))

complexes.sort()
print(len(complexes))
print('\n'.join(map(str, complexes)))

# 클로드한테 이쁘게 만들어보랬더니
"""
def dfs(y, x):
    if not (0 <= y < n and 0 <= x < n) or grid[y][x] == 0:
        return 0

    grid[y][x] = 0
    count = 1

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        count += dfs(y + dy, x + dx)

    return count

    참하게도 만들어주더라. 참고해서 풀어야겠다 앞으로. 이게 파이썬이지.
"""