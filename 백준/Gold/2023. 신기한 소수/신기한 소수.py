import sys
input = sys.stdin.readline

def is_prime(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
        
    return True


def make_prime(array):
    if len(array) == n:
        return print(''.join(array))

    now = ''.join(array)

    for i in range(1, 10):
        temp = now + str(i)

        if temp == '1':
            continue

        if is_prime(int(temp)):
            array.append(str(i))
            make_prime(array)
            array.pop()


n = int(input())
make_prime([])