import sys
input = sys.stdin.readline

p3 = [[0, 1, 1], [1, 1, 0]]
p4 = [[1, 1, 0], [0, 1, 1]]
p5 = [[0, 1, 0], [1, 1, 1]]
p6 = [[0, 0, 1], [1, 1, 1]]
p7 = [[1, 0, 0], [1, 1, 1]]

def rotation(matrix, w, h):
    turn_m = [[0] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            turn_m[j][h-1-i] = matrix[i][j]
    return turn_m

c, p = map(int, input().split())
heights = list(map(int, input().split()))
cnt = 0

if p == 1:
    cnt = c
    for i in range(c-3):
        if heights[i] == heights[i+1] == heights[i+2] == heights[i+3]:
            cnt += 1
elif p == 2:
    for i in range(c-1):
        if heights[i] == heights[i+1]:
            cnt += 1
elif p in {3, 4}:
    if p == 3:
        block = p3
    else:
        block = p4
    for i in range(c-2):
        if heights[i] + block[-1][0] == heights[i+1] + block[-1][1] == heights[i+2] + block[-1][2]:
            cnt += 1
    block = rotation(block, 3, 2)
    for i in range(c-1):
        if heights[i] + block[-1][0] == heights[i+1] + block[-1][1]:
            cnt += 1
elif p == 5:
    block = p5
    for t in range(4):
        if t & 1:
            for i in range(c-1):
                if heights[i] + block[-1][0] == heights[i+1] + block[-1][1]:
                    cnt += 1
            block = rotation(block, 2, 3)
        else:
            for i in range(c-2):
                if heights[i] + block[-1][0] == heights[i+1] + block[-1][1] == heights[i+2] + block[-1][2]:
                    cnt += 1
            block = rotation(block, 3, 2)
else:
    if p == 6:
        block = p6
    else:
        block = p7
    for t in range(4):
        if t & 1:
            if (p == 6 and t == 3) or (p == 7 and t == 1):
                for i in range(c-1):
                    if heights[i] + block[-1][0] + block[-2][0] == heights[i+1] + block[-1][1] + block[-2][1]:
                        cnt += 1
            else:
                for i in range(c-1):
                    if heights[i] + block[-1][0] == heights[i+1] + block[-1][1]:
                        cnt += 1
            block = rotation(block, 2, 3)
        else:
            for i in range(c-2):
                if heights[i] + block[-1][0] == heights[i+1] + block[-1][1] == heights[i+2] + block[-1][2]:
                    cnt += 1
            block = rotation(block, 3, 2)

print(cnt)