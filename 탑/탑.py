def solution(heights):
    answer = []
    length = len(heights)

    for idx in range(0, length):
        if idx == 0:
            answer.append(0)
            continue

        for inner_idx in range(idx-1, -1, -1):
            none = True
            if heights[inner_idx] > heights[idx]:
                answer.append(inner_idx+1)
                none = False
                break

        if none is True:
            answer.append(0)

    return answer



heights = [6,9,5,7,4]
solution(heights)