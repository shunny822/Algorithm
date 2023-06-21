def solution(plans):
    plans.sort(key=lambda x: x[1])
    uncomplete = []
    answer = []
    i = 0
    
    while i < len(plans)-1:
        name, start, running_time = plans[i]
        s = int(start[:2]) * 60 + int(start[-2:])
        next_s = int(plans[i+1][1][:2]) * 60 + int(plans[i+1][1][-2:])
        running_time = int(running_time)
        gap = next_s - s
        if gap >= running_time:
            answer.append(name)
            gap -= running_time
            while uncomplete and gap > 0:
                n, t = uncomplete.pop()
                if t <= gap:
                    answer.append(n)
                    gap -= t
                else:
                    uncomplete.append([n, t-gap])
                    break
        else:
            uncomplete.append([name, running_time-gap])
        i+= 1
    
    answer.append(plans[-1][0])
    while uncomplete:
        answer.append(uncomplete.pop()[0])
    
    return answer