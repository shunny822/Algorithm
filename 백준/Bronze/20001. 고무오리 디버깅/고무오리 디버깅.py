import sys

cnt = 0
while 1:
    s = sys.stdin.readline().rstrip()
    if s == '문제':
        cnt += 1
    elif s == '고무오리':
        if cnt == 0:
            cnt += 2
        else:
            cnt -= 1
    elif s == '고무오리 디버깅 끝':
        break

print('고무오리야 사랑해' if cnt == 0 else '힝구')