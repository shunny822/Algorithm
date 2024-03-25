import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = list(map(int, input().split()))

s = e = 0
cnt = {}
cnt[S[s]] = 1
temp = 1
ans = 0

while e < n - 1:
    e += 1
    next = S[e]
    cnt[next] = cnt.get(next, 0) + 1
    temp += 1

    if cnt[next] > k:
        while S[s] != next:
            cnt[S[s]] -= 1
            s += 1
            temp -= 1
        
        cnt[next] -= 1
        s += 1
        temp -= 1
    
    ans = max(ans, temp)

print(ans)