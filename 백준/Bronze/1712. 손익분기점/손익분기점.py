a, b, c = map(int, input().split())
print(-1 if c - b < 1 else a//(c-b) + 1)