wood = input().split()
while wood != sorted(wood):
    for i in range(4):
        if wood[i] > wood[i+1]:
            wood[i], wood[i+1] = wood[i+1], wood[i]
            print(' '.join(wood))