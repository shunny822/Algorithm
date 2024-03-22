def dfs(land, check, oil, i, j, r, c):
    check[i][j] = True
    stack = [(i, j)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    collection_x = set()
    collection_x.add(j)
    cnt = 1
    
    while stack:
        y, x = stack.pop()
        
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < r and 0 <= nx < c and land[ny][nx] and not check[ny][nx]:
                check[ny][nx] = True
                stack.append((ny, nx))
                cnt += 1
                collection_x.add(nx)

    for x in list(collection_x):
        oil[x] += cnt

def solution(land):
    r, c = len(land), len(land[0])
    oil = [0] * c
    check = [[False] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if land[i][j] and not check[i][j]:
                dfs(land, check, oil, i, j, r, c)
    
    return max(oil)