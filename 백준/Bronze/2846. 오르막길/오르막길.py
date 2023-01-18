n = int(input())
height = list(map(int, input().split()))
hill = []
boolean = True

while boolean:
    for i in range(len(height)-1):
        if height[i] >= height[i+1]:
            hill.append(height[:i+1])
            height = height[i+1:]
            break
    else:
        hill.append(height)
        boolean = False

peak = []
for h in hill:
    if len(h) > 1:
        peak.append(max(h)-min(h))

print(0 if len(peak) == 0 else max(peak))