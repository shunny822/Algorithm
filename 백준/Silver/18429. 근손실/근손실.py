import sys
input = sys.stdin.readline

def get_muscle(check, m):
    if sum(check) == n:
        cases.append(1)
        return

    for i in range(n):
        if not check[i] and m + growth[i] - k >= 0:
            check[i] = True
            get_muscle(check, m + growth[i] - k)
            check[i] = False

n, k = map(int, input().split())
growth = list(map(int, input().split()))
is_used = [False] * n
cases = []
get_muscle(is_used, 0)
print(sum(cases))