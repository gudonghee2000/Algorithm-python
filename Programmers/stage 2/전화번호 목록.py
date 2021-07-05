def solution(phone_book) :
    phone_book.sort()
    dic = {}
    for i in phone_book :
        str = ''
        for j in i :
            str += j
            if str in dic :
                return False
        dic[i] = 1
    return True