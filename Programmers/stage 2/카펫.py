def solution(brown, yellow):
    for i in range(1, yellow) :
        row = 0
        column = 0
        if yellow%i == 0:
            column += i+2
            row += yellow//i + 2
        if column*2 + row*2 -4 == brown :
            return [row, column]
    return [3,3]