def solution(s):
    zeros = 0
    change = 0
    while s != '1' :
        a = len(s)
        s = s.replace("0", "")
        b = len(s)
        zeros += a - b
        c = len(s)
        c = bin(c)
        s = c.replace("0b", "")
        change += 1
    return [change, zeros]