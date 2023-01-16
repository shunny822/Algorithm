input()
only_one = input().split()
score = total = 0
for n in only_one:
    if n == '1':
        score += 1
        total += score
    else:
        score = 0
print(total)