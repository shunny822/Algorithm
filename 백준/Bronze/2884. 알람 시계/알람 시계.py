h, m = map(int, input().split())
goal = (h*60 + m) - 45

if goal < 0:
    h = 23
    m = 60 + goal
else :
    h, m = divmod(goal, 60)

print(h, m)