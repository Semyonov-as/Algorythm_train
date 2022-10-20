def task_A(N, shirts, M, pants):
    min_val = shirts[0] - pants[0]
    min_pair = (shirts[0], pants[0])
    s_idx = 0
    p_idx = 0

    while min_val != 0 and s_idx < N and p_idx < M:
        print(f'{min_val} {min_pair} {shirts[s_idx]}-{pants[p_idx]} = {shirts[s_idx] - pants[p_idx]}')
        if abs(shirts[s_idx] - pants[p_idx]) < abs(min_val):
            min_val = shirts[s_idx] - pants[p_idx]
            min_pair = (shirts[s_idx], pants[p_idx])

        if shirts[s_idx] - pants[p_idx] > 0:
            if p_idx < M-1:
                p_idx += 1
            else:
                s_idx += 1
        else:
            if s_idx < N-1:
                s_idx += 1
            else: 
                p_idx += 1

    return min_pair

def task_A_slow(N, shirts, M, pants):
    min_val = abs(shirts[0] - pants[0])
    min_pair = (shirts[0], pants[0])
    for s in shirts:
        for p in pants:
            if abs(s-p) < min_val:
                min_val = abs(s-p)
                min_pair = (s, p)

    return min_pair
    
import random as r
def stress_test():
    ta = (0, 0)
    tas = (0, 0)
    while ta == tas:
        N = r.randint(1, 10)
        shirts = sorted([r.randint(1, 10**3) for _ in range(N)])
        M = r.randint(1, 10)
        pants = sorted([r.randint(1, 10**3) for _ in range(M)])
        print(f"N - {N} M - {M} shirts - {shirts} pants  - {pants}")

        ta = task_A(N, shirts, M, pants)
        tas = task_A_slow(N, shirts, M, pants)
        if ta != tas:
            print(f"""Stress test failed
shirts - {shirts}
pants  - {pants}
fast - {ta} 
slow - {tas}
            
            """)
    
def task_B():
    N, K = list(map(int, input().split()))
    cars = list(map(int, input().split()))

    prefixsums = [0]
    for i in range(N):
        prefixsums.append(prefixsums[-1] + cars[i])

    print(prefixsums)
    vars = 0
    l = 0
    r = 0
    while l <= N and r <= N:
        cur = prefixsums[r] - prefixsums[l]
        # print(prefixsums[r], prefixsums[l], cur,'\t', vars)

        if cur == K:
            vars += 1
            r += 1
        elif cur < K:
            r += 1
        else:
            l += 1
        
    print(vars)

def task_C():
    N = int(input())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    roads = [list(map(int, input().split())) for _ in range(M)]

    prefxsums_f = [0]
    for i in range(1, N):
        inc = mountain[i][1] - mountain[i-1][1]
        if inc > 0:
            prefxsums_f.append(prefxsums_f[-1] + inc)
        else:
            prefxsums_f.append(prefxsums_f[-1])
    prefxsums_b = [0]
    for i in range(1, N):
        inc = mountain[i][1] - mountain[i-1][1]
        if inc < 0:
            prefxsums_b.append(prefxsums_b[-1] + abs(inc))
        else:
            prefxsums_b.append(prefxsums_b[-1])

    # print(mountain)
    # print(prefxsums_f)
    # print(prefxsums_b)
    for r in roads:
        if r[1] < r[0]:
            print(prefxsums_b[r[0]-1] - prefxsums_b[r[1]-1])
        else:
            print(prefxsums_f[r[1]-1] - prefxsums_f[r[0]-1])
        
def task_E(N, K, trees):
    herbarium = dict()
    for t in trees:
        if t not in herbarium:
            herbarium[t] = 0
        herbarium[t] += 1

    l = 0
    for _ in range(N):
        if herbarium[trees[l]] > 1:
            herbarium[trees[l]] -= 1
            l += 1

    r = N-1
    for _ in range(N):
        if herbarium[trees[r]] > 1:
            herbarium[trees[r]] -= 1
            r -= 1

    herbarium = dict()
    for t in trees:
        if t not in herbarium:
            herbarium[t] = 0
        herbarium[t] += 1

    r_b = N-1
    for _ in range(N):
        if herbarium[trees[r_b]] > 1:
            herbarium[trees[r_b]] -= 1
            r_b -= 1
    l_b = 0
    for _ in range(N):
        if herbarium[trees[l_b]] > 1:
            herbarium[trees[l_b]] -= 1
            l_b += 1

    if r_b - l_b < r - l:
        print((l+1, r+1))
        print((l_b+1, r_b+1), 'back')
        return (l_b+1, r_b+1)

    # print(trees[l:r+1])
    print((l+1, r+1))
    print((l_b+1, r_b+1), 'back')
    return (l+1, r+1)


def task_E_slow(N, K, trees):
            
    def count_some(trees):
        herbarium = dict()
        for t in trees:
            if t not in herbarium:
                herbarium[t] = 0
            herbarium[t] += 1
        return herbarium

    alpha_herb = count_some(trees)
    def check_trees(herbarium):
        for k in alpha_herb:
            if k not in herbarium:
                return False

        return True

    min = N
    min_pair = (1, N)

    for l in range(N):
        for r in range(N, 0, -1):
            if check_trees(count_some(trees[l:r])) and r-l < min:
                min = r-l
                min_pair = (l+1, r)

    return min_pair

def task_E_another(N, K, trees):
    herbarium = dict()
    for k in range(1, K+1):
        herbarium[k] = 0

    def check_herb():
        for k in range(1, K+1):
            if herbarium[k] == 0:
                return False
        return True

    l, r = 0, 0
    herbarium[trees[0]] += 1
    min = N
    min_pair = (0, 0)
    for i in range(N):
        if not check_herb():
            r += 1
            herbarium[trees[r]] += 1
        else:
            break

    deleted_tree = 0
    correct = True
    while l < N:
        if herbarium[trees[l]] == 1 and correct:
            if r - l < min:
                min = r - l
                min_pair = (l+1, r+1)

            deleted_tree = trees[l]
            while r < N-1:
                r += 1
                herbarium[trees[r]] += 1
                if trees[r] == deleted_tree:
                    break
            if r == N-1 and trees[r] != deleted_tree:
                correct = False

        herbarium[trees[l]] -= 1
        l += 1

    return min_pair
        
            


                

def stress_test_E():
    te, tes = (0, 0), (0, 0)
    while te[0]-te[1] == tes[0]-tes[1]:
        n = r.randint(1, 10)
        k = r.randint(1, n)
        trees = [r.randint(0, k) for _ in range(n)]
        print(n, k, trees)
        te = task_E(n, k, trees)
        tes = task_E_slow(n, k, trees)

    print(te, tes)



if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    trees = list(map(int, input().split()))
    print(*task_E_another(N, K, trees))
    # stress_test_E()
    # print(task_E_an(8, 3, [1, 2, 0, 2, 3, 1, 3, 0]))