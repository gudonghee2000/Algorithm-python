from itertools import permutations

def check(c) :
    if c in [0, 1] :
        return False
    for i in range(2, c//2+1) :
        if c%i == 0 :
            return False
    return True

def solution(numbers):
    a = []
    for i in range(1, len(numbers)+1) :
        b = list(permutations(numbers, i))

        for j in range(len(b)) :
            c = int(''.join(b[j]))
            if check(c) and c not in a :
                a.append(c)
    return len(a)