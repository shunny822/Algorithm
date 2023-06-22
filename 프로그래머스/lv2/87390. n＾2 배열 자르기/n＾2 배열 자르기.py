def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        a, b = divmod(i, n)
        answer.append(max(a, b)+1)

    return answer

# def solution(n, left, right):
#     matrix = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(i+1):
#             matrix[i][j] = i+1
#             matrix[j][i] = i+1
    
#     arr = []
#     for line in matrix:
#         arr += line
    
#     answer = arr[left:right+1]
#     return answer