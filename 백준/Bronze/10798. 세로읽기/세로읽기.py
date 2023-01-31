import sys

words = []
new_word = ''
for _ in range(5):
    word = list(sys.stdin.readline().rstrip())
    words.append((word, len(word)))

long = sorted(words, key=lambda x: x[1])[-1][1]
for i in range(long):
    for j in range(5):
        if words[j][1]-1 < i:
            continue
        else:
            new_word += words[j][0][i]

print(new_word)