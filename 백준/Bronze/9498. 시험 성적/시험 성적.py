score = int(input())

if score < 60 or score > 100:
    grade = 'F'
elif score < 70:
    grade = 'D'
elif score < 80:
    grade = 'C'
elif score < 90:
    grade = 'B'
else :
    grade = 'A'

print(grade)