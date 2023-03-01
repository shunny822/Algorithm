import sys
intput = sys.stdin.readline

n = int(input())
farm = [tuple(map(int, input().split())) for _ in range(6)]
for i in reversed(range(6)):
    if farm[i][0] == farm[i-2][0] and farm[i-1][0] == farm[i-3][0]:
        print(n * (farm[i-4][1] * farm[i-5][1] - (farm[i-1][1] * farm[i-2][1])))