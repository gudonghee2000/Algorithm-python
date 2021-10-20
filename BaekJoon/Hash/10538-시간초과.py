h1, w1, h2, w2 = input().split()

a = []
b = []
dic = {}
answer = 0

for i in range(int(h1)) :
  a.append(list(map(str,input())))

for i in range(int(h2)) :
  b.append(list(map(str, input())))

for i in range(int(h2)) :
    tmp = {}
    for j in range(int(w2)) :
        tmp[j]= b[i][j]
    dic[i] = tmp
print(dic)

for i in range(int(h2)- int(h1)+1) :
  for j in range(int(w2)-int(w1)+1) :
    if dic[i][j] == a[0][0] :
      chk = True
      for m in range(int(h1)) :
        for t in range(1, int(w1)) :
            if dic[i+m][j+t] != a[m][t] :
                chk=False
                break
        if chk == False :
            break
      if chk == True :
        answer += 1

print(answer)



