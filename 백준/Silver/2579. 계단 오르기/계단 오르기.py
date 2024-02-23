import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]
scores = [0] * n

if n <= 2:
    print(sum(stairs[:n]))
elif n == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
else:
    scores[0] = stairs[0]
    scores[1] = stairs[0] + stairs[1]
    scores[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        scores[i] = max(stairs[i] + stairs[i-1] + scores[i-3], stairs[i] + scores[i-2])

    print(scores[-1])