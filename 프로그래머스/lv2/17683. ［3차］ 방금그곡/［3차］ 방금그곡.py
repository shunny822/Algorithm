def solution(m, musicinfos):
    answer = []
    for string in musicinfos:
        s, e, title, music_s = string.split(',')
        s_h, s_m = map(int, s.split(':'))
        e_h, e_m = map(int, e.split(':'))
        run = (e_h - s_h) * 60 + e_m - s_m
        
        i = 0
        music = []
        while i < len(music_s):
            if music_s[i] == '#':
                music[-1] += '#'
            else:
                music.append(music_s[i])
            i += 1
        
        run_music = music * (run//len(music)) + music[:run%len(music)]
        l = len(m.replace('#', ''))
        
        for j in range(len(run_music)-l+1):
            if ''.join(run_music[j:j+l]) == m:
                answer.append((title, run))
        
    
    if answer:
        answer.sort(key=lambda x: x[1], reverse=True)
        return answer[0][0]
    else:
        return '(None)'