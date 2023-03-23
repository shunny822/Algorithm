from collections import deque

def chess(check=list, l=deque, r=deque):
    global cnt

    if sum(check) == n:
        cnt += 1
        return
    
    for i in range(n):
        if not check[i] and not l[i] and not r[i]:
            check[i] = True
            l[i] = True
            r[i] = True
            a = l.popleft()
            l.append(False)
            b = r.pop()
            r.appendleft(False)
            chess(check, l, r)
            l.pop()
            l.appendleft(a)
            r.popleft()
            r.append(b)
            l[i] = False
            r[i] = False
            check[i] = False

n = int(input())
is_used = [False] * n
left = deque([False] * n)
right = deque([False] * n)
cnt = 0
chess(is_used, left, right)
print(cnt)