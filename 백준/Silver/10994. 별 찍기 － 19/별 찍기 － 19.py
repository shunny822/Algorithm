def star(n):
    if n == 1:
        return list('*')
    else:
        s_list = []
        s_list.append('*'*(4*n-3))
        s_list.append('*'+' '*(4*n-5)+'*')
        for s in star(n-1):
            s_list.append('* '+s+' *')
        s_list.append('*'+' '*(4*n-5)+'*')
        s_list.append('*'*(4*n-3))
        return s_list

print(*star(int(input())), sep='\n')