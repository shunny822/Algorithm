n = int(input())
cnt = 0
for i in range(1, n+1):
    if i < 100:
        cnt += 1
    else:
        s = str(i)
        for j in range(len(s)-2):
            if int(s[j])-int(s[j+1]) == int(s[j+1])-int(s[j+2]):
                cnt += 1
            else:
                break
print(cnt)