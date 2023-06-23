def solution(weights):
    ans = 0
    dict = {}
    
    for w in weights:
        for calc in [3/2, 2/3, 2, 1/2, 3/4, 4/3]:
            if w * calc in dict:
                ans += 1 * dict[w*calc]
        ans += dict.get(w, 0)
        dict[w] = dict.get(w, 0) + 1
    return ans