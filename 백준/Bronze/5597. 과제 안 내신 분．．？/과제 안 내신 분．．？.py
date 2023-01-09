right = []
wrong = []

for i in range(28):
    stud = int(input())
    right.append(stud)

for j in range(1, 31):
    if j not in right:
        wrong.append(j)

print(wrong[0])
print(wrong[1])