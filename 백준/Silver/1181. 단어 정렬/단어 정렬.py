import sys

n = int(input())
words = {}

for _ in range(n):
    w = sys.stdin.readline().rstrip()
    if len(w) not in words:
        words[len(w)] = {w}
    else:
        words[len(w)].add(w)

length = sorted(list(words.keys()))

for l in length:
    print(*sorted(words[l]), sep='\n')