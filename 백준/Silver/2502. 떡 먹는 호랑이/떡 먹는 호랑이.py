day, rice = map(int, input().split())
rice_div = [(1, 0), (0, 1)]
for i in range(2, day):
    rice_div.append((rice_div[i-2][0]+rice_div[i-1][0], rice_div[i-2][1]+rice_div[i-1][1]))

cnt1, cnt2 = rice_div[day-1]
n = 1
while 1:
    if (rice - (n * cnt1)) % cnt2 == 0:
        print(n, (rice - (n * cnt1))//cnt2, sep='\n')
        break
    else:
        n += 1