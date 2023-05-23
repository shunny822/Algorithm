S = list(input())
zero = S.count('0')//2
one = S.count('1')//2
z_cnt = o_cnt = 0
ans = ''

for s in S:
    if s == '0':
        if z_cnt < zero:
            ans += s
            z_cnt += 1
        else:
            continue
    else:
        if o_cnt >= one:
            ans += s
        else:
            o_cnt += 1
print(ans)