def solution(str1, str2):
    s1 = []
    s2 = []
    union = 0
    inter = 0
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            s1.append(str1[i:i + 2].upper())
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            s2.append(str2[i:i + 2].upper())
    union = len(s1) + len(s2)
    for i in s1:
        if i in s2:
            s2.remove(i)
            inter += 1
            union -= 1

    return 65536 if union == 0 else int((inter / union) * 65536)

