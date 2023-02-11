def star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        little_star = star(n//3)
        big_star = [s * 3 for s in little_star]
        for i in range(n//3):
            big_star.append(little_star[i]+' '*(n//3)+little_star[i])
        for i in range(n//3):
            big_star.append(little_star[i]*3)
        return big_star

print(*star(int(input())), sep='\n')