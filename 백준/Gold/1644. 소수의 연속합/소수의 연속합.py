import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = [True] * (n+1)

    for i in range(2, n+1):
        if nums[i]:
            temp = i * 2

            while temp < n+1:
                nums[temp] = False
                temp += i

    prime = [i for i in range(2, n+1) if nums[i]]
    l = len(prime)

    if l == 0:
        return 0

    ans = 0
    cnt = 2
    s = e = 0

    while s <= e:
        if cnt >= n:
            if cnt == n:
                ans += 1
            
            cnt -= prime[s]
            s += 1
        else:
            if e < l - 1:
                e += 1
                cnt += prime[e]
            else:
                break

    return ans


print(solve())