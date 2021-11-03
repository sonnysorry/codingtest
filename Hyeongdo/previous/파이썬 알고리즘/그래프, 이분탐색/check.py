stack = []
    stack.append(0)
    idx_list = []
    while 0 in visited:
        count = 0
        x = visited.index(0)
        if edge[x][0] > edge[x][1]:
            visited[x] = 1
            continue
        else:
            stack.append(x)
            visited[x] = 1
        while stack:
            a = stack.pop()
            for i in range(len(edge)):
                if edge[i][0] == edge[a][1] and visited[i] == 0:
                    stack.append(i)
                    count += 1
        idx_list.append(count)
    return idx_list