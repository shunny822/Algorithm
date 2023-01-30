n = int(input())
x_list = []
y_list = []
for _ in range(n):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)

matrix = [set() for _ in range(max(y_list)+10)]
for i in range(n):
    for y in range(y_list[i], y_list[i]+10):
        [matrix[y].add(x) for x in range(x_list[i], x_list[i]+10)]

total = 0
for line in matrix:
    total += len(line)
print(total)