def solution(progresses, speeds):
    answer = []
    day_count = 1

    while len(progresses) != 0:
        finish_count = 0
        while len(progresses) != 0 and progresses[0] + speeds[0] * day_count >= 100:
            progresses.pop(0)
            speeds.pop(0)
            finish_count += 1
        if finish_count != 0:
            answer.append(finish_count)
        day_count += 1

    return answer
