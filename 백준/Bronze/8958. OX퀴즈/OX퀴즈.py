t = int(input())
for i in range(t):
    ox = input()
    cnt = []
    s = 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            s += 1
            cnt.append(s)
        else:
            s = 0
    print(sum(cnt))