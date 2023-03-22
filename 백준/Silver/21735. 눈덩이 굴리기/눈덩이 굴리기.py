import sys
input = sys.stdin.readline

def roll(snow_ball, check, index):
    if sum(check) == m or index >= l:
        size.append(snow_ball)
        return
    
    check[index] = True
    roll(snow_ball + snow[index], check, index + 1)
    roll((snow_ball + snow[index])//2, check, index + 2)
    check[index] = False


n, m = map(int, input().split())
snow = list(map(int, input().split()))

if n <= m:
    print(sum(snow) + 1)
else:
    l = min(m * 2, n)
    visited = [False] * l
    size = []
    roll(1, visited, 0)
    roll(0, visited, 1)
    print(max(size))