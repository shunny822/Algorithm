import sys
input = sys.stdin.readline
from collections import deque

def D(n: int):
    return n * 2 % 10000
    

def S(n: int):
    return (n - 1 + 10000) % 10000


def L(n: int):
    return n % 1000 * 10 + n // 1000


def R(n: int):
    return n % 10 * 1000 + n // 10


def a_to_b(a: int, b: int):
    orders = [D, S, L, R]
    check = [False] * 10000
    check[a] = True
    q = deque([(a, '')])

    while q:
        n, process = q.popleft()

        if n == b:
            return print(process)
        
        for order in orders:
            temp = order(n)

            if not check[temp]:
                check[temp] = True
                q.append((temp, process + order.__name__))


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a_to_b(a, b)