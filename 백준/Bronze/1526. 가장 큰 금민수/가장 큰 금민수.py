n = int(input())
while 1:
    for c in str(n):
        if c not in ['4', '7']:
            n -= 1
            break
    else:
        break

print(n)