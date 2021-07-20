def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1) :
        line = s[:i]
        a = ''
        cnt = 1
        for j in range(i, len(s), i) :
            if line == s[j:j+i] :
                cnt += 1
            else :
                if cnt > 1:
                    a += str(cnt)
                a += line
                line = s[j:j+i]
                cnt = 1
        a += str(cnt) + line if cnt > 1 else line
        if len(a) < answer :
            answer= len(a)
    return answer