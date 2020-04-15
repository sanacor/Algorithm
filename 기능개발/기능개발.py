def solution(progresses, speeds):

    finished = len(progresses)
    point = 0
    res = []

    while True:

        for idx,  job in enumerate(progresses):
            progresses[idx] = progresses[idx] + speeds[idx]

        done_this_time = 0

        if point == finished:
            break

        for idx in range(point, finished):
            if 100 > progresses[idx]:
                break

            done_this_time += 1
            point += 1

        if done_this_time > 0:
            res.append(done_this_time)

    # print(res)
    return res


progresses = [93, 30, 55]
speeds = [1, 30, 5]

solution(progresses, speeds)
