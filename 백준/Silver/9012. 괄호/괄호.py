import sys

t = int(input())
for i in range(t):
    ps = sys.stdin.readline().rstrip()
    ps_list = []
    for j in range(len(ps)):
        if ps[j] == '(':
            ps_list.append('(')
        elif ps[j] == ')':
            if ps_list:
                ps_list.pop()
            else:
                print('NO')
                break
    else:
        print('NO' if ps_list else 'YES')