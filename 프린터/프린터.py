import queue


def solution(priorities, location):
    q = queue.Queue()

    pointer = 0
    sort = sorted(priorities, reverse=True)

    for idx, prior in enumerate(priorities):
        item = {'idx': idx, 'prior': prior}
        q.put(item)

    while True:
        if sort[pointer] == q.queue[0].get('prior'):
            pointer += 1
            v = q.get()

            if v.get('idx') == location:
                print(pointer)
                return pointer
        else:
            v = q.get()
            q.put(v)


priorities = [1, 1, 9, 1, 1, 1]
location = 0
solution(priorities, location)
