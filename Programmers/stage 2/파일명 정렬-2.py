def num_tail(file, start, end, number, tail) :
    chk = False
    for t in range(start, end) :
        if file[t].isdigit() == False or t-start == 5 :
            number.append(file[start:t])
            tail.append(file[t:end])
            chk = True
            break
    if chk == False :
        number.append(file[start: end])
        tail.append('')
def solution(files):
    head = []; number = []; tail = []
    info = []
    for i in files :
        l = len(i)
        for j in range(l) :
            if i[j].isdigit() :
                head.append(i[:j])
                num_tail(i,j,l,number,tail)
                break
        info.append([head[-1], number[-1], tail[-1]])
    info.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(i) for i in info]