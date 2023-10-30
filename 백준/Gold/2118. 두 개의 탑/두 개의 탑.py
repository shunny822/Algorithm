from sys import stdin
input = lambda: stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    dists = [int(input()) for _ in range(N)]
    ps = [0] * (2 * N + 1)
    for i in range(2 * N):
        ps[i + 1] = ps[i] + dists[i % N]

    ans = 0
    total, right = sum(dists), 1
    for left in range(2 * N):
        while right < 2 * N + 1 and ps[right] - ps[left] <= total - ps[right] + ps[left]:
            ans = max(ans, ps[right] - ps[left])
            right += 1
    print(ans)