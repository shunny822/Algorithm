import sys
intput = sys.stdin.readline

name = input().rstrip()
pal = {}

for n in name:
    if n in pal:
        pal[n] += 1
    else:
        pal[n] = 1

odd = 0
center = ''
pal_name = ''
for k, v in sorted(pal.items()):
    if v & 1:
        odd += 1
        center = k
        if odd > 1:
            print("I'm Sorry Hansoo")
            break
    pal_name += k * (v//2)
else:
    print(pal_name, center, pal_name[::-1], sep='')