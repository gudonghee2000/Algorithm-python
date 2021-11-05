def finder(place) :
    info = []
    for i in range(5) :
        for j in range(5) :
            if place[i][j] == 'P' :
                info.append([i, j, 0])
    return info

def bfs(place) :
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visit = [[False for _ in range(5)] for _ in range(5)]
    info = finder(place)
    queue = []
    if info :
        queue.append(info.pop(0))
    while queue :
        r, c, dist = queue.pop(0)
        visit[r][c] = True
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            ndist = dist + 1
            if nr < 0 or nc < 0 or nr >= 5 or nc >= 5 :
                continue
            if ndist > 2 :
                continue
            if place[nr][nc] == 'P' and visit[nr][nc] == False :
                return False
            elif place[nr][nc] == 'O' and visit[nr][nc] == False :
                queue.append([nr, nc, ndist])
        if not queue and info :
            queue.append(info.pop(0))
    return True

def solution(places):
    answer = []
    for place in places :
        if bfs(place) :
            answer.append(1)
        else :
            answer.append(0)
    return answer