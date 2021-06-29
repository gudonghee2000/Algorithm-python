def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]
              }
    left = [3, 0]
    right = [3, 2]

    for i in numbers:
        if i in [1, 4, 7]:
            left = keypad[i]
            answer += 'L'
        elif i in [3, 6, 9]:
            right = keypad[i]
            answer += 'R'
        else:
            l_len = abs(keypad[i][0] - left[0]) + abs(keypad[i][1] - left[1])
            r_len = abs(keypad[i][0] - right[0]) + abs(keypad[i][1] - right[1])
            if l_len > r_len:
                right = keypad[i]
                answer += 'R'
            elif r_len > l_len:
                left = keypad[i]
                answer += 'L'
            else:
                if hand == 'right':
                    right = keypad[i]
                    answer += 'R'
                else:
                    left = keypad[i]
                    answer += 'L'

    return answer