def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        for v, j in stack:
            answer[j] += 1
            
        while stack and stack[-1][0] > prices[i]:
            stack.pop()
        stack.append((prices[i], i))
    
    return answer