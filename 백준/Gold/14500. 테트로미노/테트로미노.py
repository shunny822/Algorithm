import sys
input = sys.stdin.readline

def dfs(y, x, paper, ans, block, total):
    if len(block) == 4:
        return max(ans, total)

    delta = [(1, 0), (0, -1), (0, 1)]

    for dy, dx in delta:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in block:
            block.append((ny, nx))
            temp = paper[ny][nx]
            total += temp
            ans = dfs(ny, nx, paper, ans, block, total)

            if len(block) == 3:
                ans = dfs(y, x, paper, ans, block, total)

            block.pop()
            total -= temp

    return ans

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = []

for i in range(n):
    for j in range(m):
        ans.append(dfs(i, j, paper, 0, [(i, j)], paper[i][j]))

print(max(ans))