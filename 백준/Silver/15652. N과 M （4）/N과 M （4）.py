def generator(combi=list, num=int):
    if len(combi) == m:
        return print(*combi)
    
    for i in range(num, n+1):
        combi.append(i)
        generator(combi, i)
        combi.pop()

n, m = map(int, input().split())
generator([], 1)