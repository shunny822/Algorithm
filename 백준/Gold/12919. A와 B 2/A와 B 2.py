import sys
input = sys.stdin.readline

def switch(t):
    if len(t) == l:
        if t == S:
            possible.append(1)
        return
    
    if t[-1] == 'A':
        switch(t[:len(t)-1])
    if t[0] == 'B':
        switch(t[len(t)-1:0:-1])

S = input().rstrip()
T = input().rstrip()
l = len(S)
possible = []
switch(T)
print(1 if possible else 0)