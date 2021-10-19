import sys
sys.setrecursionlimit(10**8)

def isValid(land, row, column) :
    if 0 > row or row >= len(land) or column < 0 or column >=len(land[0]) :
        return False
    return True

def dfs(land, row, column) :
  if 0 > row or row >= len(land) or column < 0 or column >=len(land[0]) :
    return
  if land[row][column] == 1 :
    land[row][column] = -1
    if isValid(land, row+1, column) :
        dfs(land, row+1, column)
    if isValid(land, row-1, column) :
        dfs(land, row-1, column)
    if isValid(land, row, column+1) :
        dfs(land, row, column+1)
    if isValid(land, row, column-1) :
        dfs(land, row, column-1)

t = int(input())
for i in range(t):
  m, n, k = map(int, input().split())
  land = [[0 for _ in range(m)] for _ in range(n)]
  answer = 0
  for j in range(k) :
    c, r = map(int, input().split())
    land[r][c] = 1
  for j in range(n) :
    for t in range(m) :
      if land[j][t] == 1 :
        dfs(land, j, t)
        answer += 1
  print(answer)