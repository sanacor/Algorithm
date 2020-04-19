def solution(arrangement):
    length = len(arrangement)
    bundle = 0
    cnt = 0
    idx = 0
    # for idx in range(0, length):
    while True:
        if check_razer(arrangement, idx) is True:
            cnt += bundle
            idx += 2
        elif arrangement[idx] == '(':
            bundle += 1
            idx += 1
        elif arrangement[idx] == ')':
            cnt += 1
            bundle -= 1
            idx += 1

        if idx == length:
            break

    # print(cnt)
    return cnt


def check_razer(arrangement, idx):
    try:
        if arrangement[idx:idx+2] == '()':
            return True

        return False

    except IndexError:
        return False

arrangement = "()(((()())(())()))(())"

solution(arrangement)