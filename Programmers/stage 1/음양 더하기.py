def solution(a, signs):
    return sum([a[i] for i in range(len(a)) if signs[i] == True]) + sum([-a[i] for i in range(len(a)) if signs[i] == False])