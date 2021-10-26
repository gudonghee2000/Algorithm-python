def solution(genres, plays):
    answer = []
    music_len = len(plays)
    number_dic = {}
    total_play_dic = {}
    for i in range(music_len) :
        number_dic[i] = [genres[i], plays[i]]
        if genres[i] not in total_play_dic :
            total_play_dic[genres[i]] = plays[i]
        else :
            total_play_dic[genres[i]] += plays[i]
    total_play_dic = sorted(total_play_dic.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(total_play_dic)) :
        tmp = []
        for j in range(len(number_dic)) :
            if total_play_dic[i][0] == number_dic[j][0] :
                tmp.append([j, number_dic[j][1]])
        tmp.sort(key = lambda x : x[1], reverse=True)
        tmp = [item[0] for item in tmp]
        tmp = tmp[:2]
        for t in tmp :
            answer.append(t)
    return answer