def solution(files):
    ret = []
    for f in files :
        new_file = []
        for i in range(len(f)) :
            if f[i].isdigit() :
                new_file.append(f[:i])
                for j in range(i, i+6) :
                    if len(f) == j :
                        new_file.append(f[i:j])
                        break
                    elif f[j].isdigit() == False :
                        new_file.append(f[i:j])
                        new_file.append(f[j:])
                        break
                break
        ret.append(new_file)
    ret.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(r) for r in ret]