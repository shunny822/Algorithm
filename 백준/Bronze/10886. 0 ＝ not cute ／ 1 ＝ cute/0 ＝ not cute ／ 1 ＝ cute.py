t = int(input())
one = zero = 0

for i in range(t):
    if int(input()):
        one += 1
    else:
        zero += 1
result = 'Junhee is cute!' if one > zero else 'Junhee is not cute!'
print(result)