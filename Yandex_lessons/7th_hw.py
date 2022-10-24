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
        # events.append([students[i] - D, -1]) #start of interval
        events.append([students[i] + D + 1, -1]) # end of interval of var i
        events.append([students[i], 0, i]) # for count

    events.sort()

    s_v = []
    var_st = []
    popped = None
    max_v = 0
    for e in events:
        if e[1] == 0:
            if popped != None and len(var_st) > 0:
                var_st.append(popped)
                popped = None
            else:
                var_st.append(len(var_st)+1)
            s_v.append((e[2], var_st[-1]))
        else:
            max_v = max(max_v, len(var_st))
            popped = var_st.pop(0)

    s_v.sort()
    # print(s_v)
    print(max_v)
    print(' '.join([str(i[1]) for i in s_v]))
    
def task_D():
    N = int(input())
    events = []
    for i in range(N):
        c_in, c_out = map(int, input().split()) 
        if c_out - c_in >= 5:
            events.append((c_in, -1, i))
            events.append((c_out - 5, 1, i))
    events.sort()

    if len(events) == 0:
        print(0, 5, 10)
    elif len(events) == 2:
        print(1, events[0][0], events[0][0]+5)
    else:
        firstad = set()
        best = 0
        ad1, ad2 = 0, 0
        for i in range(len(events)):
            e1 = events[i]
            if e1[1] == -1:
                firstad.add(e1[2])
                if len(firstad) > best:
                    best = len(firstad)
                    ad1, ad2 = e1[0], e1[0]+5
            seccnt = 0
            for j in range(i+1, len(events)):
                e2 = events[j]
                if e2[1] == -1 and e2[2] not in firstad:
                    seccnt += 1
                if e2[0] - e1[0] >= 5 and len(firstad) + seccnt > best:
                    best = len(firstad) + seccnt
                    ad1, ad2 = e1[0], e2[0]
                if e2[1] == 1 and e2[2] not in firstad:
                    seccnt -= 1
            if e1[1] == 1:
                firstad.remove(e1[2])

        print(best, ad1, ad2)

def task_E():
    n = int(input())
    events = []
    for i in range(n):
        h1, m1, h2, m2 = map(int, input().split())
        if h1 == h2 and m1 == m2:
            events.append(((0, 0), -1, i)) 
            events.append(((24, 0), 1, i))
        else:
            events.append(((h1, m1), -1, i)) 
            events.append(((h2, m2), 1, i))

    events.sort()
    cur_open = set()
    for i in range(len(events)):
        e = events[i]
        if e[1] == -1:
            cur_open.add(e[2])
        if e[1] == 1 and e[2] in cur_open:
            cur_open.remove(e[2])
    all_t = 0
    for i in range(len(events)):
        e = events[i]
        if e[1] == -1:
            cur_open.add(e[2])
        if e[1] == 1 and e[2] in cur_open:
            if len(cur_open) == n:
                h = e[0][0] - events[i-1][0][0]
                m = e[0][1] - events[i-1][0][1]
                all_t += m + h*60
            cur_open.remove(e[2])

    print(all_t)
        
def task_F():
    from datetime import date, timedelta
    N = int(input())
    events = []
    for i in range(1, N+1):
        d1, m1, y1, d2, m2, y2 = map(int, input().split())
        bd = date(y1, m2, d1)
        md = date(y1+18, m1, d1)
        od = date(y1+80, m1, d1) - timedelta(1)
        ripd = date(y2, m2, d2)
        if ripd > md:
            events.append((md, -1, i))
            if ripd > od:
                events.append((od, 1, i))
            else:
                events.append((ripd, 1, i))

    events.sort()
    if len(events) == 0:
        print(0)
    else:
        cur_s = set()
        max_p = []
        c_max = 0
        for e in events:
            if e[1] == -1:
                cur_s.add(e[2])
            if e[1] == 1:
                c_max = max(len(cur_s), c_max)
                cur_s.remove(e[2])
            if len(cur_s) == 0:
                max_p.append(c_max)
                c_max = 0

        for e in events:
            if e[1] == -1:
                cur_s.add(e[2])
            if e[1] == 1:
                if len(cur_s) == max_p[0]:
                    print(*cur_s)
                    max_p.pop(0)
                    if len(max_p) == 0:
                        break
                cur_s.remove(e[2])
        
def task_G():
    M, N = map(int, input().split())
    workers = []
    for i in range(1, N+1):
        t, z, y = map(int, input().split())
                                    #t_work, t_rest, cnt_work, cnt_total
                    #   0   1  2  3  4       5       6         7
        workers.append([t, -z, y, i, 0, 0, 0, 0])
    workers.sort()
    t = 0
    while M > 0:
        for w in workers:
            if (t - w[4] >= w[0] or not w[4]) and (t - w[5] >= w[2] or not w[5]):
                if w[6] < -w[1]:
                    w[4] = t
                    w[6] += 1
                    w[7] += 1
                    M -= 1
                else:
                    w[5] = t
                    w[6] = 0
            if M == 0:
                break
        t += 1
            
    print(t)
    print(' '.join([str(w[7]) for w in sorted(workers, key=lambda x: x[3])]))


def task_H():
    K = int(input())

    for i in range(K):
        arr = list(map(int, input().split()))
        N = arr[0]
        events = []
        for i in range(N):
            events.append((arr[2*i+1], -1, i))
            events.append((arr[2*i+2], 1, i))

        events.sort()

        cnt = set()
        solo = set()
        flag = True
        for i in range(len(events)):
            if cnt == 0 and i != 0:
                flag = False
                break
            if len(cnt) == 1 and events[i][0] - events[i-1][0] > 0:
                solo.update(cnt)
            if events[i][1] == -1:
                cnt.add(events[i][2])
            if events[i][1] == 1:
                cnt.remove(events[i][2])

        if len(solo) != N or events[-1][0] != 10000:
            flag = False

        if flag:
            print('Accepted')
        else:
            print('Wrong Answer')

def task_I():
    pass

def task_J():
    pass

if __name__ == "__main__":
    task_H()
