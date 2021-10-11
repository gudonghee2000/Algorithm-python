def solution(people, limit):
    answer = 0
    start= 0
    end = len(people) -1
    people.sort(reverse = True)
    while start <= end :
        boat = 0
        boat += people[start]
        start += 1
        if people and boat + people[end] <= limit :
            boat += people[end]
            end -= 1
        answer += 1
    return answer