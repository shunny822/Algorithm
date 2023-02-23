room_n = input()
number = {i: 0 for i in range(10)}

for n in room_n:
    n = int(n)
    if n in [6, 9]:
        if number[6] < number[9]:
            number[6] += 1
        else:
            number[9] += 1
    else:
        number[n] += 1

v = list(number.values())
print(max(v))