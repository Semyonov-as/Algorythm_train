def task_A():
    N, M = list(map(int, input().split()))
    preps = [list(map(int, input().split())) for _ in range(M)]

    events = []
    for p in preps:
        events.append((p[0], -1)) #start watching
        events.append((p[1]+1, 1)) #stop watching

    events.sort()

    at_least_one = 0
    cur_w = 0
    for i in range(len(events)):
        if cur_w > 0:
            at_least_one += events[i][0] - events[i-1][0]
        cur_w -= events[i][1]

    print(N - at_least_one)

if __name__ == "__main__":
    task_A()