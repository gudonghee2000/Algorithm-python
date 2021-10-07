def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1) :
        cnt = 1
        ret = ''
        word = ''
        for j in range(0, len(s), i) :
            if word == '' or s[j:j+i] != word :
                if cnt > 1 :
                    ret += (str(cnt) + word)
                else :
                    ret += word
                word = s[j:j+i]
                cnt = 1
            else :
                cnt += 1
        if cnt > 1 :
            ret += str(cnt) + word
        else :
            ret += word
        if answer > len(ret) :
            answer = len(ret)
    return answer