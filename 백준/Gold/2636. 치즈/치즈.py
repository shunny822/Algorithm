import sys
input = sys.stdin.readline

def melt(melting, turn):
    result = len(melting)
    new_melting = []

    while melting:
        y, x = melting.pop()
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if ny >= 0 and ny < r and nx >= 0 and nx < c:
                if not check[ny][nx]:
                    check[ny][nx] = True
                    if cheese[ny][nx] == 0:
                        melting.append((ny, nx))
                    else:
                        new_melting.append((ny, nx))
    if new_melting:
        return melt(new_melting, turn + 1)
    else:
        return turn, result

r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(r)]
check = [[False] * c for _ in range(r)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
check[0][0] = True
print(*melt([(0, 0)], 0), sep='\n')