def dfs(start, graph, visit) :
  global answer
  visit[start] = -1
  for i in graph[start] :
    if visit[i] == 0 :
      answer += 1
      dfs(i, graph, visit)

n = int(input())
cnt = int(input())

graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

answer = 0
connect = []

for i in range(cnt) :
  coms = input().split(' ')
  connect.append([int(c)for c in coms])

for c in connect :
  graph[c[0]].append(c[1])
  graph[c[1]].append(c[0])

dfs(1, graph, visit)
print(answer)