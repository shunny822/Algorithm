def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    ans = len(word)
    for i in range(len(word)):
        n = vowels.index(word[i])
        ans += n
        calc = n
        for j in range(4-i):
            calc *= 5
            ans += calc
            
    return ans