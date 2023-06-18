def solution(picks, minerals):
    answer = 0
    level = []
    
    for i in range(0, min(sum(picks)*5, len(minerals)), 5):
        cnt = 0
        for j in range(5):
            if i + j >= len(minerals):
                break
            x = minerals[i+j]
            if x == 'diamond':
                cnt += 25
            elif x == 'iron':
                cnt += 5
            else:
                cnt += 1
        level.append((cnt, i))
    level.sort(key=lambda x: x[0], reverse=True)
    
    for cnt, i in level:
        for j in range(3):
            if picks[j] > 0:
                picks[j] -= 1
                tool = j
                break
        
        for k in range(5):
            if i + k >= len(minerals):
                break
            if minerals[i+k] == 'diamond':
                mineral = 0
            elif minerals[i+k] == 'iron':
                mineral = 1
            else:
                mineral = 2
            
            if tool > mineral:
                answer += 5 ** (tool-mineral)
            else:
                answer += 1
                
    return answer