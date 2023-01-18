remove_s = 'CAMBRIDGE'
input_s = input()
result = []

for i in range(len(input_s)):
    if input_s[i] not in remove_s:
        result.append(input_s[i])
print(''.join(result))