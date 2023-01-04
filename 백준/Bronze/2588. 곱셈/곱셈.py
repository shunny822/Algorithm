first = int(input())
second = int(input())

a = str(second)[0]
b = str(second)[1]
c = str(second)[2]

print(first*int(c), first*int(b), first*int(a), first*second, sep='\n')