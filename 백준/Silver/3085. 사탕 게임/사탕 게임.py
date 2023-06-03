import sys
input = sys.stdin.readline

def explore(board):
    global n

    uni = 0
    res = 0
    for i in range(n):
        if board[i] == board[i][0] * n:
            if uni == 0:
                uni += 1
                res = max(res, n-1)
                continue
            else:
                res = n
                break
        chance = 1
        cnt = 0
        candy = ''
        for j in range(n):
            if cnt == 0:
                candy = board[i][j]
                cnt += 1
                res = max(res, cnt)
            else:
                if board[i][j] == candy:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    if chance:
                        for dy in [-1, 1]:
                            ny = i + dy
                            if 0 <= ny < n and board[ny][j] == candy:
                                chance = 0
                                cnt += 1
                                res = max(res, cnt)
                                break
                        else:
                            if j + 1 < n and board[i][j+1] == candy:
                                cnt += 1
                                res = max(res, cnt)
                            cnt = 1
                            candy = board[i][j]
                    else:
                        cnt = 1
                        candy = board[i][j]
                        chance = 1
    return res

def swap(board):
    turn_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turn_board[i][j] = board[n-1-j][i]
    return turn_board


n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]
ans = []

for _ in range(4):
    ans.append(explore(matrix))
    matrix = swap(matrix)
print(max(ans))