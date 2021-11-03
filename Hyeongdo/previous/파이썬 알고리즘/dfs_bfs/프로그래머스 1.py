def dfs(numbers, target):
    depth = 0
    if depth > len(numbers):
        numbers[depth] *= 1
        dfs(numbers, target, depth + 1)

        numbers[depth] *= -1
        dfs(numbers, target, depth + 1)

    elif sum(numbers) == target:
        count += 1