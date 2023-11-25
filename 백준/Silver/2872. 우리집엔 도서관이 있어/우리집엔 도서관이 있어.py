import sys
input = sys.stdin.readline

n = int(input())
books = [int(input()) for _ in range(n)]
compare = n - 1
cnt = 1

for i in reversed(range(0, books.index(n))):
    if books[i] == compare:
        cnt += 1
        compare -= 1

print(n - cnt)