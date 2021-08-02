def changeAlpha(m) :
    while "#" in m :
        index = m.index("#")
        if index > -1 :
            m[index-1] = m[index-1].lower()
            del m[index]
    m = ''.join(m)
    return m

def chkTime(start, end) :
    time1 = int(start[:2])*60 + int(start[3:])
    time2 = int(end[:2])*60 + int(end[3:])
    return time2 - time1

def solution(m, musicinfos):
    ret = []
    m = changeAlpha(list(m))
    for info in musicinfos :
        codes = ''
        std = info.split(',')
        std[3] = changeAlpha(list(std[3]))
        time = chkTime(std[0], std[1])
        while time >= len(std[3]) :
            codes += std[3]
            time -= len(std[3])
        codes += std[3][:time]
        if m in codes :
            if not ret :
                ret.append([len(codes), std[2]])
            elif len(codes) > ret[0][0] :
                ret.pop(0)
                ret.append([len(codes), std[2]])
    return "(None)" if not ret else ret[0][1]