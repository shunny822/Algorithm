import sys

n, m = map(int, input().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
fix_cnt = []

for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        # if board[i][j] == 'W':
        for a in range(i, i+8, 2):
            cnt += board[a][j:j+8:2].count('B')
            cnt += board[a][j+1:j+8:2].count('W')
        for b in range(i+1, i+8, 2):
            cnt += board[b][j:j+8:2].count('W')
            cnt += board[b][j+1:j+8:2].count('B')
        fix_cnt.append(cnt)
        fix_cnt.append(64-cnt)

print(min(fix_cnt))