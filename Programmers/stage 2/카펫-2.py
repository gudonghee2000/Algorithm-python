def solution(brown, yellow):
    r = yellow
    c = 1
    divider = 2
    while r >= c:
        b_row = (r+2)*2
        b_column = (c+2)*2
        new_brown = b_row + b_column - 4
        if new_brown == brown :
            return [r+2, c+2]
        if yellow%divider == 0 :
            r = yellow//divider
            c = yellow//r
        divider += 1
    return -1