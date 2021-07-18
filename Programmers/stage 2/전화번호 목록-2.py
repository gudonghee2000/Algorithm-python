def solution(phone_book):
    dic = {}
    phone_book.sort(key=lambda x: len(x))
    for i in phone_book:
        dic[i] = 1

    for i in dic.keys():
        tmp = ''
        for t in range(len(i)):
            tmp += i[t]
            if tmp in dic and tmp != i:
                return False
    return True
