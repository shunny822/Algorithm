import sys
input = sys.stdin.readline
from collections import deque

def copy_num():
    if board[dice[0]][dice[1]] == 0:
        board[dice[0]][dice[1]] = dice_y[3]
    else:
        dice_y[3] = board[dice[0]][dice[1]]
        dice_x[3] = dice_y[3]
        board[dice[0]][dice[1]] = 0


def roll_dice(order):
    dy, dx = delta[order-1]
    ny, nx = dice[0] + dy, dice[1] + dx

    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        return
    
    dice[0], dice[1] = ny, nx
    
    if order == 1:
        dice_x.appendleft(dice_x.pop())
        dice_y[1] = dice_x[1]
        dice_y[3] = dice_x[3]
    elif order == 2:
        dice_x.append(dice_x.popleft())
        dice_y[1] = dice_x[1]
        dice_y[3] = dice_x[3]
    elif order == 3:
        dice_y.append(dice_y.popleft())
        dice_x[1] = dice_y[1]
        dice_x[3] = dice_y[3]
    else:
        dice_y.appendleft(dice_y.pop())
        dice_x[1] = dice_y[1]
        dice_x[3] = dice_y[3]
    
    copy_num()
    print(dice_y[1])


n, m, y, x, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in  range(n)]
orders = list(map(int, input().split()))

dice = [y, x]
dice_y = deque([0, 0, 0, 0])
dice_x = deque([0, 0, 0, 0])
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for order in orders:
    roll_dice(order)