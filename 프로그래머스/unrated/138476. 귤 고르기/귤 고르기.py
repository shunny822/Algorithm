def solution(k, tangerine):
    mandarin = {}
    for size in tangerine:
        mandarin[size] = mandarin.get(size, 0) + 1
    
    m_cnt = list(mandarin.values())
    m_cnt.sort(reverse=True)
    
    answer = 0
    for n in m_cnt:
        k -= n
        answer += 1
        if k <= 0:
            break
    
    return answer