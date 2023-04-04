import sys
input = sys.stdin.readline

vowel = {'a', 'e', 'i', 'o', 'u'}
while 1:
    password = input().rstrip()
    if password == 'end':
        break

    cnt = 1
    is_impossible = False
    if password[0] in vowel:
        is_vowel = True
        include_v = True
    else:
        is_vowel = False
        include_v = False

    for i in range(1, len(password)):
        if (password[i] == password[i-1]) and (password[i] not in {'e', 'o'}):
            is_impossible = True
            break
        
        if password[i] in vowel:
            include_v = True
            if is_vowel:
                cnt += 1
            else:
                cnt = 1
            is_vowel = True
        else:
            if is_vowel:
                cnt = 1
            else:
                cnt += 1
            is_vowel = False
        
        if cnt == 3:
            is_impossible = True
            break
    
    if include_v and not is_impossible:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')