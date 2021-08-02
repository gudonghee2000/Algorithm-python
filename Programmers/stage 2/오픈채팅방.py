def solution(record):
    dic = {}
    ret = []
    for i in record :
        std = i.split()
        if std[0] in ['Enter', 'Change'] :
            dic[std[1]] = std[2]
    for i in record :
        std2 = i.split()
        if std2[0] == 'Enter' :
            ret.append(dic[std2[1]] + "님이 들어왔습니다.")
        elif std2[0] == 'Leave' :
            ret.append(dic[std2[1]] + "님이 나갔습니다.")
    return ret