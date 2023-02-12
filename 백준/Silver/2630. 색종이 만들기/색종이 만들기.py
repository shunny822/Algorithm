import sys

def what_color(copy_p):
    l = len(copy_p)
    is_differ = False

    for y in range(l):
        for x in range(l):
            if copy_p[y][x] != copy_p[0][0]:
                is_differ = True
                break
        if is_differ:
            break
    else:
        if copy_p[0][0]:
            white_blue[1] += 1
        else:
            white_blue[0] += 1
        return

    if is_differ:
        for i in range(0, l, l//2):
            for j in range(0, l, l//2):
                div_p = [copy_p[k][j:j+l//2] for k in range(i, i+l//2)]
                what_color(div_p)

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white_blue = [0, 0]
what_color(paper)
print(*white_blue, sep='\n')