import sys

while 1:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    pair = []
    for s in string:
        if s in ['(', '[']:
            pair.append(s)
        elif s in [')', ']']:
            if pair:
                if s == ')' and pair[-1] == '(':
                    pair.pop()
                elif s == ']' and pair[-1] == '[':
                    pair.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        print('no' if pair else 'yes')
