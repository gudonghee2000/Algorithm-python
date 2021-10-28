n = int(input())
students = {}
for i in range(1, (n ** 2) + 1):
    students[i] = 0

input_students = [list(map(int, input().split())) for _ in range(n ** 2)]


def second_condi(table, j, t, friend):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    cnt = 0
    for i in range(4):
        nx = j + dx[i]
        ny = t + dy[i]
        if nx < 0 or ny < 0 or nx >= len(table) or ny >= len(table):
            continue
        if table[nx][ny] == -1:
            cnt += 1
    return cnt


def first_condi(table, j, t, friend):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    cnt = 0
    for i in range(4):
        nx = j + dx[i]
        ny = t + dy[i]
        if nx < 0 or ny < 0 or nx >= len(table) or ny >= len(table):
            continue
        if table[nx][ny] in friend:
            cnt += 1
    return cnt


def bfs(table, i):
    start = i[0]
    friend = list(i[1:len(i)])
    first = 0
    second = 0
    r = []
    c = []
    blank = []
    for j in range(len(table)):
        for t in range(len(table)):
            if table[j][t] == -1:
                first_cnt = first_condi(table, j, t, friend)
                if first_cnt != 0 and first < first_cnt:
                    first = first_cnt
    for j in range(len(table)):
        for t in range(len(table)):
            if table[j][t] == -1:
                first_cnt = first_condi(table, j, t, friend)
                if first_cnt != 0 and first == first_cnt:
                    r.append(j)
                    c.append(t)
    if len(r) == 1 and len(c) == 1:
        return [r[0], c[0]]
    if r == [] and c == []:
        new_r, new_c = 0, 0
        for j in range(len(table)):
            for t in range(len(table)):
                if table[j][t] == -1:
                    second_cnt = second_condi(table, j, t, friend)
                    if second_cnt != 0 and second < second_cnt:
                        new_r = j
                        new_c = t
                        second = second_cnt
        return [new_r, new_c]
    else:
        dr, dc = r[0], c[0]
        for j in range(len(r)):
            nr = r[j]
            nc = c[j]
            second_cnt = second_condi(table, nr, nc, friend)
            if second_cnt != 0 and second < second_cnt:
                dr = nr
                dc = nc
                second = second_cnt

        return [dr, dc]


def answer(N, input):
    answer = 0
    table = [[-1 for _ in range(N)] for _ in range(N)]

    for i in input:
        pos = bfs(table, i)
        table[pos[0]][pos[1]] = i[0]
    for x in range(len(table)):
        for y in range(len(table)):
            for i in input:
                start = i[0]
                friend = i[1:len(i)]
                if table[x][y] == start:
                    dx = [1, -1, 0, 0]
                    dy = [0, 0, -1, 1]
                    cnt = 0
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or ny < 0 or nx >= len(table) or ny >= len(table):
                            continue
                        if table[nx][ny] in friend:
                            cnt += 1
                    if cnt >= 1:
                        answer += (10) ** (cnt - 1)
                    break
    return answer


ret = answer(n, input_students)
print(ret)