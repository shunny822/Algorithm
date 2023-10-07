import sys
input = sys.stdin.readline

def make_password(l, s, e, chars, password, v, nv):
    if len(password) == l:
        if v > 0 and nv > 1:
            print(''.join(password))
        return
    
    for i in range(s, e):
        password.append(chars[i])
        if chars[i] in {'a', 'e', 'i', 'o', 'u'}:
            make_password(l, i+1, e+1, chars, password, v+1, nv)
        else:
            make_password(l, i+1, e+1, chars, password, v, nv+1)
        password.pop()

l, c = map(int, input().split())
chars = input().split()
chars.sort()
make_password(l, 0, c-l+1, chars, [], 0, 0)