def solution(s):
    ret = ''
    for i in range(1, len(s)//2 +1) :
        word = ''
        compression = ''
        count = 0
        for j in range(0, len(s), i) :
            if compression == '' or compression != s[j:j+i] :
                if count > 1 :
                    word += str(count)
                word += compression
                compression = s[j:j+i]
                count = 1
            elif compression == s[j:j+i] :
                count += 1
        if count > 1 :
            word += str(count)
        word += compression
        if ret == '' or len(ret) > len(word) :
            ret = word
    return len(ret) if ret != '' else 1