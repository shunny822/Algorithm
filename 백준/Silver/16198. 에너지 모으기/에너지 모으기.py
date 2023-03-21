import sys
input = sys.stdin.readline

def energe(check, total):
    if sum(check) == n-2:
        result.append(total)
        return
    
    for i in range(1, n-1):
        if not check[i]:
            check[i] = True
            a = b = i
            while check[a]:
                a -= 1
            while check[b]:
                b += 1
            energe(check, total + balls[a] * balls[b])
            check[i] = False

n = int(input())
balls = list(map(int, input().split()))
is_used = [False] * n
result = []
energe(is_used, 0)
print(max(result))