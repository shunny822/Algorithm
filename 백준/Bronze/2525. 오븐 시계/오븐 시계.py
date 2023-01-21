a, b = map(int, input().split())
time = int(input())
end = a*60 + b + time

if end >= 24*60 :
    end -= 24*60

a, b = divmod(end, 60)
print(a, b)