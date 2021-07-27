def solution(s):
    cnt = 0
    remove = 0
    while s != '1' :
        zero_cnt = s.count('0')
        remove += zero_cnt
        s = bin(len(s) - zero_cnt)[2:]
        cnt += 1
    return [cnt, remove]