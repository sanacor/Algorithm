def solution(answers):
    answer = []

    one_rule = {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5
    }
    two_rule = {
        0: 2,
        1: 1,
        2: 2,
        3: 3,
        4: 2,
        5: 4,
        6: 2,
        7: 5,
    }
    three_rule = {
        0: 3,
        1: 3,
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 4,
        7: 4,
        8: 5,
        9: 5
    }

    one, two, three = 0, 0, 0

    cnt = {
        1: 0,
        2: 0,
        3: 0
    }
    for idx, sol in enumerate(answers):
        if sol == one_rule[(idx % 5)]:
            cnt[1] += 1
        if sol == two_rule[(idx % 8)]:
            cnt[2] += 1
        if sol == three_rule[(idx % 10)]:
            cnt[3] += 1

    if cnt[1] == cnt[2] == cnt[3]:
        return [1, 2, 3]
    elif cnt[1] >= cnt[2] >= cnt[3]:
        if cnt[1] == cnt[2]:
            return [1, 2]
        return [1]
    elif cnt[1] >= cnt[3] >= cnt[2]:
        if cnt[1] == cnt[3]:
            return [1, 3]
        return [1]
    elif cnt[2] >= cnt[1] >= cnt[3]:
        if cnt[2] == cnt[1]:
            return [1, 2]
        return [2]
    elif cnt[2] >= cnt[3] >= cnt[1]:
        if cnt[2] == cnt[3]:
            return [2, 3]
        return [2]
    elif cnt[3] >= cnt[1] >= cnt[2]:
        if cnt[3] == cnt[1]:
            return [3, 1]
        return [3]
    elif cnt[3] >= cnt[2] >= cnt[1]:
        if cnt[3] == cnt[2]:
            return [3, 2]
        return [3]
