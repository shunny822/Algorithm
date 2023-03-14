import itertools

rome = [1, 5, 10, 50]
case_n = set()
for nums in itertools.combinations_with_replacement(rome, int(input())):
    case_n.add(sum(nums))

print(len(case_n))