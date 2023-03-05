import sys
intput = sys.stdin.readline

formula = input().split('-')
result = sum(map(int, formula[0].split('+')))
for i in range(1, len(formula)):
    result -= sum(map(int, formula[i].split('+')))

print(result)