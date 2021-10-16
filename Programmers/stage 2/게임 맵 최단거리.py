def solution(maps):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    r, c = 0, 0

    table = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    table[r][c] = 1

    queue = []
    queue.append([r, c])

    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr > len(maps) - 1 or nc > len(maps[0]) - 1:
                continue
            if maps[nr][nc] == 1 and table[nr][nc] == -1:
                table[nr][nc] = table[r][c] + 1
                queue.append([nr, nc])

    return table[len(maps) - 1][len(maps[0]) - 1]