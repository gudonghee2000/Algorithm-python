def checkPlayTime(start, end) :
    start = start.split(':')
    end = end.split(':')
    return (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))

def makeMusicCode(musicCode, playTime) :
    codes = []
    for i in range(playTime) :
        i = i%len(musicCode)
        codes.append(musicCode[i])
    return ''.join(codes)

def replaceCodes(musicCodes) :
    return musicCodes.replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g').replace("A#", 'a')

def solution(m, musicinfos):
    answer = ''
    answer_playTime = 0
    m = replaceCodes(m)
    for musicinfo in musicinfos :
        infos = musicinfo.split(',')
        title = infos[2]
        playTime = checkPlayTime(infos[0], infos[1])
        infos[3] = replaceCodes(infos[3])
        musicCode = makeMusicCode(infos[3], playTime)
        if m in musicCode :
            if answer == '' or answer_playTime < playTime :
                answer = title
                answer_playTime = playTime
    return "(None)" if not answer else answer