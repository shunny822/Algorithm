import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [[0] * c for _ in range(r)]
for i in range(r):
    line = list(input().rstrip())
    for j in range(c):
        if line[j] == 'O':
            board[i][j] = 2
        else:
            board[i][j] = 0

n -= 1
for t in range(n):
    for i in range(r):
        for j in range(c):
            board[i][j] += 1
    if t & 1:
        check = [[False] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] > 3:
                    check[i][j] = True
                    for dy, dx in delta:
                        ny = i + dy
                        nx = j + dx
                        if ny >= 0 and ny < r and nx >= 0 and nx < c:
                            if not check[ny][nx]:
                                check[ny][nx] = True
        for i in range(r):
            for j in range(c):
                if check[i][j]:
                    board[i][j] = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print()