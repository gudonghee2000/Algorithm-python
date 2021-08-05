def solution(genres, plays):
    dic = {}
    answer = []
    music_l = len(genres)

    for l in range(music_l) :
        if genres[l] in dic :
            dic[genres[l]] += plays[l]
        else :
            dic[genres[l]] = plays[l]
    sdic = sorted(dic.items(), key = lambda x : -x[1])
    for key in sdic :
        music = []
        for i in range(music_l) :
            if genres[i] == key[0] :
                music.append([plays[i], i])
        music.sort(key = lambda x : -x[0])
        cnt = 0
        for m in music :
            if cnt == 2 :
                break
            answer.append(m[1])
            cnt += 1
    return answer