def solution(want, number, discount):
    ans = 0
    my_things = {}
    for i in range(10):
        my_things[discount[i]] = my_things.get(discount[i], 0) + 1
    
    for i in range(len(want)):
        if number[i] != my_things.get(want[i], 0):
            break
    else:
        ans += 1

    
    s = 0
    for i in range(10, len(discount)):
        my_things[discount[i]] = my_things.get(discount[i], 0) + 1
        if my_things[discount[s]] == 1:
            my_things.pop(discount[s])
        else:
            my_things[discount[s]] -= 1
        s += 1
        
        for j in range(len(want)):
            if number[j] != my_things.get(want[j], 0):
                break
        else:
            ans += 1
    
    return ans