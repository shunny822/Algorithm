import sys

y = list(reversed(range(1, 9)))
x = [chr(i) for i in range(65, 73)]
move = {
    'R': (1, 0), 
    'L': (-1, 0),
    'B': (0, 1),
    'T': (0, -1), 
    'RT': (1, -1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (-1, 1)
}

k, s, n = sys.stdin.readline().split()
king = (x.index(k[0]), 8-int(k[1]))
stone = (x.index(s[0]), 8-int(s[1]))

for i in range(int(n)):
    order = move[sys.stdin.readline().rstrip()]
    if 0 <= king[0]+order[0] < 8 and 0 <= king[1]+order[1] < 8:
        if stone == (king[0]+order[0], king[1]+order[1]):
            if 0 <= stone[0]+order[0] < 8 and 0 <= stone[1]+order[1] < 8:
                king = (king[0]+order[0], king[1]+order[1])
                stone = (stone[0]+order[0], stone[1]+order[1])
            else:
                continue
        else:
            king = (king[0]+order[0], king[1]+order[1])
    else:
        continue

print(x[king[0]], y[king[1]], sep='')
print(x[stone[0]], y[stone[1]], sep='')