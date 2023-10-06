import sys
input = sys.stdin.readline

def make_lotto(s, e, nums, lotto):
    if (len(lotto) == 6 ):
        print(' '.join(lotto))
        return

    for i in range(s, e):
        lotto.append(nums[i])
        make_lotto(i+1, e+1, nums, lotto)
        lotto.pop()

while 1:
    arr = input().split()
    # print('arr: ', arr)
    if arr[0] == '0': break

    k = arr[0]
    nums = arr[1:]
    make_lotto(0, int(k)-5, nums, [])
    print()