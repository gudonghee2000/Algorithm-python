def check(words, index) :
    for i in range(index) :
        if words[index] == words[i] :
            return False
    return True

def solution(n, words):
    turn = 1
    number = 1
    for i in range(len(words)-1) :
        if (i+1)%n == 0:
            turn += 1
            number = 1
        else :
            number += 1
        if words[i][-1] != words[i+1][0] or check(words, i+1) == False :
            return [number, turn]
    return [0, 0]