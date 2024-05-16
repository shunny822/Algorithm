import sys
input = sys.stdin.readline

def check_road(board):
    cnt = 0

    for i in range(n):
        runway = [False] * n

        for j in range(1, n):
            if board[i][j] > board[i][j-1]:
                if board[i][j] - board[i][j-1] != 1:
                    break

                is_impossible = False

                for k in range(1, l+1):
                    if j - k < 0 or runway[j-k] or board[i][j-k] != board[i][j-1]:
                        is_impossible = True
                        break
                
                if is_impossible:
                    break
                else:
                    for k in range(1, l+1):
                        runway[j-k] = True

            elif board[i][j] < board[i][j-1]:
                if board[i][j-1] - board[i][j] != 1:
                    break

                is_impossible = False

                for k in range(l):
                    if j + k >= n or runway[j+k] or board[i][j+k] != board[i][j]:
                        is_impossible = True
                        break
                
                if is_impossible:
                    break
                else:
                    for k in range(l):
                        runway[j+k] = True
        else:
            cnt += 1

    return cnt


n, l = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
new_matrix = [[0] * n for _ in range(n)]

res = check_road(matrix)

for i in range(n):
    for j in range(n):
        new_matrix[j][i] = matrix[i][j]

res += check_road(new_matrix)
print(res)