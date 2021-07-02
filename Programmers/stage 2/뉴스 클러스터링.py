def solution(str1, str2):
    a = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    b = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
    c = []
    d = a + b
    f = [True for i in range(len(b))]

    for i in a:
        for j in range(len(b)):
            if i == b[j] and f[j] == True:
                f[j] = False
                c.append(i)
                break

    for i in c:
        for j in range(len(d) - 1, -1, -1):
            if d[j] == i:
                del d[j]
                break

    if not d: return 65536
    return (len(c) / len(d)) * 65536 // 1