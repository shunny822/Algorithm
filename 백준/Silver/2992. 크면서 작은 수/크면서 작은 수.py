def generator(n, u):
    if sum(u) == l:
        nums.add(n)
        return
    else:
        for i in range(l):
            if not u[i]:
                u[i] = True
                generator(n + x[i], u)
                u[i] = False

x = input()
l = len(x)
used = [False] * l
nums = set()

generator('', used)
numbers = sorted(list(nums))
i = numbers.index(x)
print(numbers[i+1] if i + 1 < len(nums) else 0)