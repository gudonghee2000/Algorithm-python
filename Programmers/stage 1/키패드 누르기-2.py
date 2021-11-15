def solution(numbers, hand):
    ret = ''
    left = [3,0]
    right = [3,2]
    for n in numbers :
        print(left, right)
        f = n//3
        if n%3 == 0 :
            f -= 1
            s = 2
        else :
            s = n%3 - 1
        if n == 0 :
            f, s = 3, 1
        if n in [1,4,7] :
            left = [f, s]
            ret += 'L'
        elif n in [3,6,9] :
            right = [f, s]
            ret += 'R'
        elif n in [2,5,8,0] :
            if abs(left[0] - f) + abs(left[1] - s) > abs(right[0] - f) + abs(right[1] - s) :
                right = [f, s]
                ret += 'R'
            elif abs(left[0] - f) + abs(left[1] - s) == abs(right[0] - f) + abs(right[1] - s) :
                if hand == "right" :
                    right = [f, s]
                    ret += 'R'
                else :
                    left = [f, s]
                    ret += 'L'
            else :
                left = [f, s]
                ret += 'L'
    return ret