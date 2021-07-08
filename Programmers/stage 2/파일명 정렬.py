def solution(files):
    answer = []
    for i in files:
        tmp = []
        for j in range(len(i)):
            if i[j].isdigit() == True:
                tmp.append(i[:j])
                i = i[j:]
                break
        length = 5 if len(i) >= 5 else len(i)

        for j in range(length):
            if i[j].isdigit() == False:
                tmp.append(i[:j])
                i = i[j:]
                break
            elif j == 4:
                tmp.append(i[:j + 1])
                i = i[j + 1:]
                break
        tmp.append(i)
        answer.append(tmp)
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(i) for i in answer]