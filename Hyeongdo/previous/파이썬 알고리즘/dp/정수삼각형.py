triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(0, i+1):
            if j == i:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            elif j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(triangle[-1])
    return answer

print(solution(triangle))