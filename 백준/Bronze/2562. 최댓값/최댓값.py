numbers = []
for i in range(9):
    number = input()
    numbers.append(int(number))

big_num = max(numbers)
print(big_num)
print(numbers.index(big_num)+1)