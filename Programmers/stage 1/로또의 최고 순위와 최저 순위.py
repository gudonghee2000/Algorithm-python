def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()

    same = [i for i in lottos for j in win_nums if i == j]
    zero = [i for i in lottos if i == 0]

    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    return [dic[len(same) + len(zero)], dic[len(same)]]