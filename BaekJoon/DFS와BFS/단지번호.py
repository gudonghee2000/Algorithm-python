n = int(input())
table = []
visit = [[0 for _ in range(n)] for _ in range(n)]
answer_cnt = 0
answer_array = []

for i in range(n) :
  table.append(list(map(int, input())))

queue = []
dr = [1,-1,0,0]
dc = [0,0,1,-1]

for i in range(len(table)) :
  for j in range(len(table[i])):
    if table[i][j] == 1 and visit[i][j] == 0 :
      queue.append([i, j])
      visit[i][j] = -1
      cnt = 1
      while queue :
        r, c = queue.pop(0)
        for t in range(4) :
          nr = r + dr[t]
          nc = c + dc[t]
          if 0>nr or nr>=n or 0>nc or nc>=n :
            continue
          if visit[nr][nc] == 0 and table[nr][nc] == 1 :
            queue.append([nr, nc])
            visit[nr][nc] = -1
            cnt += 1
      answer_array.append(cnt)
      answer_cnt += 1

print(answer_cnt)
answer_array.sort()
for a in answer_array :
  print(a)