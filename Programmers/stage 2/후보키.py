from itertools import combinations

def solution(relation):
    rows = len(relation)
    columns = len(relation[0])

    all_key = []
    for i in range(1, columns + 1):
        all_key.extend(combinations(range(columns), i))

    unique_key = []
    for a in all_key:
        s = set()
        for r in relation:
            s.add(''.join([r[item] for item in a]))
        if len(s) == rows:
            unique_key.append(a)

    answer = set(unique_key)
    for i in range(len(unique_key)):
        for j in range(i + 1, len(unique_key)):
            if len(unique_key[i]) == len(set(unique_key[i]) & set(unique_key[j])):
                answer.discard(unique_key[j])

    return len(answer)