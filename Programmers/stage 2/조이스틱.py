def check(a):
    for i in a:
        if i != 0:
            return False
    return True
def solution(name):
    a = [ord(i)-65 for i in name]
    cnt = 0
    pos = 0
    while True :
        cnt += 26-a[pos] if a[pos] > 13 else a[pos]
        a[pos] = 0
        right = 1; left = 1
        if check(a) :
            break
        while a[pos+right] == 0 :
            right += 1
        while a[pos-left] == 0:
            left += 1
        pos = pos-left if right > left else pos+right
        cnt += left if right > left else right
    return cnt
