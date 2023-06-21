from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    answer = 0
    
    if (sum_q1 + sum(q2)) & 1:
        return -1
    else:
        target = (sum_q1 + sum(q2)) // 2
        l = len(q1)
        while answer <= l * 4:
            if sum_q1 < target:
                x = q2.popleft()
                q1.append(x)
                sum_q1 += x
            elif sum_q1 > target:
                x = q1.popleft()
                q2.append(x)
                sum_q1 -= x
            else:
                return answer
            answer += 1

    return -1