n = int(input())
table = input().split()
m = int(input())
table2 = input().split()
answer = []
dic = {}

for t in table :
  dic[t] = 1

for t in table2 :
  if t in dic :
    answer.append(1)
  else :
    answer.append(0)

for a in answer :
  print(a)