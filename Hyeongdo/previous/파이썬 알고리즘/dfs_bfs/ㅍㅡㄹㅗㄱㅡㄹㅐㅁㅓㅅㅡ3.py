# dfs로 작
def dfs(begin, target, words):
    # 스택 생성
    stack = [begin]
    # path 리스트 생
    visited = [0 for i in range(len(words))]
    # 타겟 넘버가 words 안에 없으면 0 리턴
    if not target in words: return 0
    # 타겟이 있으면, 타겟 삭제하고 맨 처음으로 보냄.
    # 뒤에 있으면 되게 복잡한 패스 들어갈 수도 있음.
    if target in words:
        words.remove(target)
        words.insert(0,target)
    # 값 초기화
    answer = 0
    # 스택이 빌 때 까지 지속 (dfs)
    while stack:
        node = stack.pop()
        # 조건 - 노드가 타겟과 같으면 answer 리턴
        if node == target:
            return answer
        # 그 외에는 한 글자가 다르면 아래 코드 실행
        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != node[j]]) == 1 and visited[i] == 0:
                visited[i] = 1
                stack.append(words[i])
                print(words[i])
                answer += 1
                break;
    return answer
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(dfs(begin, target, words))