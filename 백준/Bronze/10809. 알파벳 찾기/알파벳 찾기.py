alpha = list(map(chr, range(97, 123)))
s = input()
for a in alpha:
    print(s.find(a), end=' ')