x, y, w, h = map(int, input().split())
l = []
l.append(w-x) if x > w - x else l.append(x)
l.append(h-y) if y > h - y else l.append(y)
print(min(l))