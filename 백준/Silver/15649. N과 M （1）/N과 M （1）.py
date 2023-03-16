def generator(ck, combi=list):
    if len(combi) == m:
        return print(*combi)
    for i in range(1, n+1):
        if not ck[i]:
            ck[i] = True
            combi.append(i)
            generator(ck, combi)
            ck[i] = False
            combi.pop()

n, m = map(int, input().split())
check = [False] * (n+1)
check[0] = True
combi_n = []
generator(check, combi_n)