def explore(index, cards, c):
    stack = [cards[index]]
    c[index] = True
    cnt = 1
    while stack:
        x = stack.pop()
        if not c[x-1]:
            c[x-1] = True
            stack.append(cards[x-1])
            cnt += 1
    return cnt, c
    

def solution(cards):
    game = []
    
    check = [False] * len(cards)
    for i in range(len(cards)):
        if not check[i]:
            n, check = explore(i, cards, check)
            game.append(n)
    
    first = max(game)
    first_i = game.index(first)
    second = 0
    
    for i in range(len(game)):
        if i != first_i and game[i] > second:
            second = game[i]
    
    return first * second