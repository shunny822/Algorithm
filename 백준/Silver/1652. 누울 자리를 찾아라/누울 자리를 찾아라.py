import sys

n = int(input())
room = [sys.stdin.readline() for _ in range(n)]
t_site = 0
v_site = 0
for i in range(n):
    for j in room[i].split('X'):
        if '..' in j:
            t_site += 1

turn_room = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        turn_room[i][j] = room[j][i]

for i in range(n):
    turn_room[i] = ''.join(turn_room[i])
for i in range(n):
    for j in turn_room[i].split('X'):
        if '..' in j:
            v_site += 1

print(t_site, v_site)