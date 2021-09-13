import re

def solution(s):
    ret = []
    numbers = re.compile("}+,+").split(s)
    for i in range(len(numbers)) :
        numbers[i] = numbers[i].replace("{","").replace("}","").split(",")
    numbers.sort(key=lambda x : len(x))
    for n in numbers :
        for j in range(len(n)) :
            if int(n[j]) not in ret :
                ret.append(int(n[j]))
    return ret