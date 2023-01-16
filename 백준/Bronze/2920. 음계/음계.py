notes = list(map(int, input().split()))
for i in range(len(notes)-1):
    if abs(notes[i] - notes[i+1]) != 1:
        print('mixed')
        break
else:
    print('ascending' if notes[0] == 1 else 'descending')