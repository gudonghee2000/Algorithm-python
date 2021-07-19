def solution(msg):
    table = {}
    answer = []
    line = ''; pos = 27
    for i in range(26) :
        table[chr(65+i)] = i+1
    for i in range(len(msg)) :
        line += msg[i]
        if line not in table :
            answer.append(table[line[:-1]])
            table[line] = pos
            pos += 1
            line = msg[i]
    answer.append(table[line])
    return answer