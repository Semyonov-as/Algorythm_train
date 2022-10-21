def task_A():
    N, K = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    K_list = list(map(int, input().split()))

    for k in K_list:
        l = 0
        r = N - 1
        if k < N_list[0] or k > N_list[-1]:
            print('NO')
        elif k == N_list[0] or k == N_list[-1]:
            print('YES')
        else:
            # print('While loop')
            # print(N_list, k)
            while l < r:
                m = (r + l)//2
                # print(f"{'>'*10} l={l} r={r} m={m}")
                if N_list[m] >= k:
                    r = m
                else:
                    l = m + 1

            # print(N_list[l], r)
            if N_list[l] == k:
                print('YES')
            else:
                print('NO')

def task_B():
    N, K = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    K_list = list(map(int, input().split()))

    for k in K_list:
        l = 0
        r = N - 1

        while l < r:
            m = (r+l)//2
            # print('>'*10, N_list[m], k)
            if N_list[m] >= k:
                r = m
            else:
                l = m + 1
        # print('>'*20, N_list[l])
        cmp =N_list[l] - k
        if l >= 1 and k - N_list[l-1] <= cmp:
            # print('>'*20, N_list[l-1])
            print(N_list[l-1])
        else:
            print(N_list[l])

def task_C():
    w, h, n = list(map(int, input().split()))

    l = 0
    r = n*(w if w > h else h)
    while l < r:
        m = (r + l)//2
        # print(f'l={l} m={m} r={r} {m//w*(m//h)}')
        if m//w*(m//h) >= n:
            r = m
        else:
            l = m + 1

    print(l)

def task_D(n, a, b, w, h):
    # n, a, b, w, h = list(map(int, input().split()))
    l = 0
    r = n*(w if w > h else h)
    # if w//a*(h//b) <= n:
    #     print(0)
    # else:
    while l < r:
        m = (r + l + 1)//2
        # print(f'l={l} m={m} r={r} {m//w*(m//h)}')
        if (w//(a+2*m))*(h//(b+2*m)) >= n:
            l = m
        else:
            r = m - 1

    return l

from math import sqrt
def precise_task_D(n, a, b, w, h):
    n, a, b, w, h = list(map(float, (n, a, b, w, h)))
    D = sqrt((a-b)**2 + 4*w*h/n)
    d = (-(a+b)+D)/4
    return d, int(d if d > 0 else 0)

def task_E():
    a = int(input())
    b = int(input())
    c = int(input())

    l = 0
    r = a + b + c

    if (a*2 + b*3 + c*4)/(a + b + c ) >= 3.5:
        print(0)
    else:
        while l < r:
            m = (r + l)//2

            if (a*2 + b*3 + c*4 + m*5)/(a + b + c + m) >= 3.5:
                r = m
            else:
                l = m + 1

        print(r)

def task_I(N, R, C, students):
    # N, R, C = list(map(int, input().split()))
    # students = sorted([int(input()) for _ in range(N)])
    # print(students)
    def check(x):
        num_r = 0
        i = 0
        while i < N-C+1:
            # print('>'*10, students[i+C], students[i])
            if students[i+C-1] - students[i] <= x:
                # print(students[i: i + C])
                num_r += 1
                i += C 
            else:
                i += 1
        
        return num_r >= R

    l = 0
    r = students[-1] - students[0]

    while l < r:
        m = (l + r)//2

        if check(m):
            r = m
        else:
            l = m + 1

    return(l)

def task_I_slow(N, R, C, students):
    # N, R, C = list(map(int, input().split()))
    # students = sorted([int(input()) for _ in range(N)])

    min_uneq = students[-1] - students[0]

    for i in range(N-R*C):
        cur_max = 0
        r = 0
        for j in range(i, N-C, C):
            # print('>'*20, students[j: j+C])
            tmp = students[j+C-1] - students[j]
            r += 1
            cur_max = tmp if tmp > cur_max else cur_max
            if r == R:
                r = 0
                min_uneq = cur_max if cur_max < min_uneq else min_uneq
            
        # print('-'*10, cur_max)
        if r == R:
            min_uneq = cur_max if cur_max < min_uneq else min_uneq

    return(min_uneq)

def task_J_slow(): #but actually it 3 times faster than binary search
    N, L = list(map(int, input().split()))
    arrs = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            tmp = sorted(arrs[i]+ arrs[j])
            print(tmp[L-1])

def task_J():
    N, L = list(map(int, input().split()))
    arrs = [list(map(int, input().split())) for _ in range(N)]

    def check(med, arr1, arr2):
        cnt = 0
        for a in arr1:
            if a > med:
                break
            cnt += 1
        for a in arr2:
            if a > med:
                break
            cnt += 1
        return cnt >= L

    for i in range(N):
        for j in range(i+1, N):
            l = min(arrs[i][0], arrs[j][0])
            r = max(arrs[i][-1], arrs[j][-1])

            while l < r:
                m = (l+r)//2
                if check(m, arrs[i], arrs[j]):
                    r = m
                else:
                    l = m + 1

            print(l)
    
def task_K():
    N, L = list(map(int, input().split()))
    arrs_coeffs = [list(map(int, input().split())) for _ in range(N)]

    def make_arr(coeffs):
        x1, d1, a, c, m = coeffs
        arr = [x1]
        d_prev = d1
        for i in range(L-1):
            arr.append(arr[-1] + d_prev)
            d_prev = (a*d_prev+c)%m

        return arr

    arrs = [make_arr(x) for x in arrs_coeffs]
    # [print(arr) for arr in arrs]

    def check(med, arr1, arr2):
        def rbs(arr):
            l = 0
            r = L-1
            while l < r:
                m = (r+l+1)//2
                if arr[m] <= med:
                    l = m
                else:
                    r = m - 1
            return l+1
        return rbs(arr1)+rbs(arr2) >= L

    for i in range(N):
        for j in range(i+1, N):
            l = min(arrs[i][0], arrs[j][0])
            r = max(arrs[i][-1], arrs[j][-1])

            while l < r:
                m = (l+r)//2
                if check(m, arrs[i], arrs[j]):
                    r = m
                else:
                    l = m + 1

            print(l)

from random import randint
from scipy.optimize import brentq
if __name__ == "__main__":
    # task_K()
    task_J()