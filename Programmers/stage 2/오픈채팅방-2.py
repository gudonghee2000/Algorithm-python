def solution(record):
    dic = {}
    answer = []
    for i in range(len(record)) :
        info = record[i].split(" ")
        if info[0] in [ "Enter", "Change" ] :
            dic[info[1]] = info[2]
    for i in range(len(record)) :
        info = record[i].split(" ")
        if info[0] == "Enter" :
            answer.append(dic[info[1]] + "님이 들어왔습니다.")
        elif info[0] == "Leave" :
            answer.append(dic[info[1]] + "님이 나갔습니다.")
    return answer