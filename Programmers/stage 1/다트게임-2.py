def solution(dartResult):
    point = []
    for i in range(0, len(dartResult)) :
        if dartResult[i].isdigit() == True :
            if i >= 1 and dartResult[i-1].isdigit() == True :
                continue
            if len(dartResult) > i+1 and dartResult[i+1].isdigit() == True :
                point.append(int(dartResult[i:i+2]))
            else :
                point.append(int(dartResult[i]))
        elif dartResult[i] == 'D' :
            point[-1] = point[-1] ** 2
        elif dartResult[i] == 'T' :
            point[-1] = point[-1] ** 3
        elif dartResult[i] == '*' :
            point[-1] = point[-1] * 2
            if len(point) >= 2 :
                point[-2] = point[-2] * 2
        elif dartResult[i] == '#' :
            point[-1] = -point[-1]
    return sum(point)