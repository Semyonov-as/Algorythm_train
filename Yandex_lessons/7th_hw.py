from random import randint

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

def task_B(N, M, cuts, points):
    # N, M = list(map(int, input().split()))
    # cuts = [list(map(int, input().split())) for _ in range(N)]
    # points = list(map(int, input().split()))

    events = []
    for c in cuts:
        a = c[0]
        b = c[1]
        if a > b:
            a, b = b, a
        events.append((a, 1)) #start
        events.append((b+1, -1)) #end
    for i, p in enumerate(points):
        events.append((p, 2, i))#points to find

    events.sort()

    cur_cuts = 0
    ans = ['']*M
    for e in events:
        if e[1] == 2:
            ans[e[2]] = str(cur_cuts)
        else:
            cur_cuts += e[1]

    return ' '.join(ans)


def task_B_s(N, M, cuts, points):
    # N, M = list(map(int, input().split()))
    # cuts = [list(map(int, input().split())) for _ in range(N)]
    # points = list(map(int, input().split()))

    ans = []
    for p in points:
        cnt = 0
        for c in cuts:
            if p >= c[0] and p <= c[1]:
                cnt += 1
        ans.append(str(cnt))

    return ' '.join(ans)

def stress_B():
    print('Stress test started')
    while True:
        
        N = randint(0, 100)
        M = randint(0, 100)
        cuts = []
        for i in range(N):
            a = randint(-100, 1000)
            b = randint(-1000, 100)
            if a > b:
                a, b = b, a
            cuts.append([a, b])
        points = [randint(-1000, 1000) for _ in range(M)]
        b = task_B(N, M, cuts, points)
        bs = task_B_s(N, M, cuts, points)
        if b != bs:
            print('Failing test case:')
            print((N, M, cuts, points), b, '--', bs)
            break


def task_C_s():
    N, D = list(map(int, input().split()))
    students = list(map(int, input().split()))

    print(students)
    talking = []
    max_talk = 0
    for i in range(N):
        cnt_talking = 0
        for j in range(N):
            if abs(students[i]-students[j]) <= D and students[i]!=students[j]:
                cnt_talking += 1
        talking.append(cnt_talking)
        if cnt_talking > max_talk:
            max_talk = cnt_talking
    print(max_talk+1)
    print(talking)

def task_C():
    N, D = list(map(int, input().split()))
    students = list(map(int, input().split()))
    events = []
    for i in range(N):
        events.append((students[i] - D, -1, 0, i))

"""
6 2
11 1 12 2 3 4 
"""

def task_D():
    pass

def task_E():
    pass

def task_F():
    pass

def task_G():
    pass

def task_H():
    pass

def task_I():
    pass

def task_J():
    pass

if __name__ == "__main__":
    task_C_s()
