def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers = sorted(numbers, key = lambda x : x*3, reverse=True)
    return str(int(''.join(numbers)))