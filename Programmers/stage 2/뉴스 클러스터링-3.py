import re

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]',str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]',str2[i:i+2])]
    inter = []
    for s in str1 :
        if s in str2 :
            str2.remove(s)
            inter.append(s)
    union = str1 + str2
    return (len(inter)/len(union)) * 65536 // 1 if len(union) > 0 else 65536