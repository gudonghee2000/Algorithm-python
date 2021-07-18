from itertools import permutations

def check(num) :
    for i in range(2, num//2+1) :
        if num%i == 0 :
            return False
    return True
def solution(numbers):
    numbers = list(numbers)
    n = set()
    cnt = 0
    for i in range(1, len(numbers)+1) :
        a = list(permutations(numbers,i))
        for j in a :
            s = int(''.join(j))
            n.add(s)
    for i in n :
        if i > 1 and check(i) :
            cnt += 1
    return cnt
