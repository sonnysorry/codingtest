def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if (sum(numbers)) == target:
            answer += 1
            return
    else:
        numbers[depth] *= 1
        dfs(numbers, target, depth + 1)
        numbers[depth] *= -1
        dfs(numbers, target, depth + 1)


def solution(numbers, target):
    answer = 0
    dfs(numbers, target, 0)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))