from collections import deque

n = int(input())
card = deque(range(1, n+1))
for i in range(n-1):
    print(card.popleft(), end=' ')
    card.append(card.popleft())
print(card.popleft())