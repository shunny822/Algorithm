import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
rec = list(map(int, input().split()))
vote = {}
seq = []

for i in range(m):
    if rec[i] in vote:
        vote[rec[i]] += 1
    else:
        if len(vote) == n:
            min_vote = min(vote.values())
            for j in range(len(seq)):
                if vote[seq[j]] == min_vote:
                    vote.pop(seq[j])
                    seq.pop(j)
                    break
            
        vote[rec[i]] = 1
        seq.append(rec[i])

print(*sorted(vote.keys()))