def solution(s):
    answer = []
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, }
    dic2 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, }
    a = ""

    for spell in s:
        a += spell
        if a in dic:
            answer.append(dic[a])
            a = ""
        elif a in dic2:
            answer.append(dic2[a])
            a = ""

    return int("".join([str(a) for a in answer]))
