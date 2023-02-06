import sys

s = sys.stdin.readline()
happy_s = s.replace(':-)', '')
sad_s = s.replace(':-(', '')
happy = (len(s)-len(happy_s))
sad = (len(s)-len(sad_s))

if happy or sad:
    if happy > sad:
        print('happy')
    elif sad > happy:
        print('sad')
    else:
        print('unsure')
else:
    print('none')