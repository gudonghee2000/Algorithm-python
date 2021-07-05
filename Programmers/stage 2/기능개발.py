def solution(progresses, speeds):
    answer = []
    c = 0
    while progresses :
        c += 1
        if progresses[0]+ speeds[0]*c >= 100 :
            ret = 0
            while progresses:
                progresses.pop(0)
                speeds.pop(0)
                ret += 1
                if not progresses or progresses[0]+ speeds[0]*c < 100 :
                    answer.append(ret)
                    break
    return answer