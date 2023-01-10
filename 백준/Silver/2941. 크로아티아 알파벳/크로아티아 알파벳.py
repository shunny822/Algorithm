word = input()
croa = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for a in croa:
    if a in word:
        word = word.replace(a, '1')

print(len(word))