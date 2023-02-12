import sys

def what_color(y, x, l):
    global white, blue
    is_differ = False
    
    for i in range(l):
        for j in range(l):
            if paper[y+i][x+j] != paper[y][x]:
                is_differ = True
                break
        if is_differ:
            break
    
    if is_differ:
        l //= 2
        what_color(y, x, l)
        what_color(y, x+l, l)
        what_color(y+l, x, l)
        what_color(y+l, x+l, l)
    else:
        if paper[y][x]:
            blue += 1
        else:
            white += 1
        return

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = blue = 0
what_color(0, 0, n)
print(white, blue, sep='\n')