def solution(id):
    id = id.lower()
    new_id = list(id)

    for i in range(len(new_id) - 1, -1, -1):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in ['-', '_', '.']:
            continue
        del new_id[i]

    for i in range(len(new_id) - 1, 0, -1):
        if new_id[i] == '.' and new_id[i - 1] == '.':
            del new_id[i]

    if new_id and new_id[0] == '.':
        del new_id[0]
    if new_id and new_id[len(new_id) - 1] == '.':
        del new_id[len(new_id) - 1]

    if not new_id:
        new_id.append('a')
    elif len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[len(new_id) - 1] == '.':
        del new_id[len(new_id) - 1]

    if len(new_id) <= 2:
        a = new_id[len(new_id) - 1]
        while len(new_id) < 3:
            new_id += a

    return ''.join(new_id)
