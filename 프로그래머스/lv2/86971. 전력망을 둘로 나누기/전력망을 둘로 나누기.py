from collections import deque


def bfs(arr, cut):
    check = [False] * len(arr)
    q = deque([1])
    check[1] = True
    cnt = 1
    
    while q:
        x = q.popleft()
        for connect in arr[x]:
            if connect in cut and x in cut:
                check[connect] = True
            if not check[connect]:
                check[connect] = True
                q.append(connect)
                cnt += 1
    return cnt


def solution(n, wires):
    matrix = [[] for _ in range(n+1)]
    for w in wires:
        a, b = w
        matrix[a].append(b)
        matrix[b].append(a)
    
    wires.sort(key=lambda x: x[1])
    ans = 100
    for w in wires:
        first = bfs(matrix, w)
        second = n - first
        ans = min(ans, abs(first-second))
    
    return ans