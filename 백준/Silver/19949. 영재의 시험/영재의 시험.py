import sys
input = sys.stdin.readline

def generator(my_answer=list, score=int):
    global cases

    l = len(my_answer)
    if score + 10 - l < 5:
        return
    elif l == 10 and score >= 5:
        cases += 1
        return
    
    if l > 1 and my_answer[-1] == my_answer[-2]:
        for i in range(1, 6):
            if i == my_answer[-1]:
                continue
            else:
                my_answer.append(i)
                if i == answer[len(my_answer)-1]:
                    generator(my_answer, score + 1)
                else:
                    generator(my_answer, score)
                my_answer.pop()
    else:
        for i in range(1, 6):
            my_answer.append(i)
            if i == answer[len(my_answer)-1]:
                generator(my_answer, score + 1)
            else:
                generator(my_answer, score)
            my_answer.pop()

answer = list(map(int, input().split()))
cases = 0
generator([], 0)
print(cases)