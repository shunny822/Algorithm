import sys

n, m = map(int, input().split())
number = list(map(int, sys.stdin.readline().split()))
blackjack = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            three_n = number[i] + number[j] + number[k]
            if (three_n <= m) and (three_n > blackjack):
                blackjack = three_n

print(blackjack)