from itertools import product

def solution(word):
    alpha = 'AEIOU'
    dic = []
    word = tuple(word)
    for i in range(1, 6) :
        dic += list(product(alpha, repeat=i))
    dic.sort()
    return dic.index(word)+1