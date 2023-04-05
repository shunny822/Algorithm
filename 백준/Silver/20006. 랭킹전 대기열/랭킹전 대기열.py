import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room = []

for _ in range(p):
    l, n = input().rstrip().split()
    l = int(l)

    for r in room:
        if r:
            if len(r) < m and l >= r[0][0] - 10 and l <= r[0][0] + 10:
                r.append((l, n))
                break
    else:
        room.append([(l, n)])

for i in range(len(room)):
    if len(room[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    for r in sorted(room[i], key=lambda x: x[1]):
        print(*r)