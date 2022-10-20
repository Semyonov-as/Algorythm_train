def task_D():
    n = int(input())
    keys_press = list(map(int, input().split()))    
    k = int(input())
    press = list(map(int, input().split()))  


    keys = dict()
    for i, p in enumerate(keys_press):
        keys[i+1] = p

    for p in press:
        keys[p] -= 1

    for i in range(n):
        if keys[i+1] >= 0:
            print('NO')
        else: 
            print('YES')

def task_E():
    N = int(input())
    wh = dict()

    for i in range(N):
        w, h = list(map(int, input().split()))
        if w not in wh:
            wh[w] = []
        wh[w].append(h)

    def get_max_h(arr):
        max = arr[0]
        for item in arr:
            if item > max:
                max = item
        return max

    w_sorted = sorted(list(wh.keys()))

    prev = 0
    height = 0
    for w in w_sorted:
        if w > prev:
            prev = w
            height += get_max_h(wh[w])

    print(height)

def task_H():
    glen, Slen = list(map(int, input().split()))
    g = input()
    S = input()

    def count_sym(in_str):
        ans = dict()
        for c in in_str:
            if c not in ans:
                ans[c] = 0
            ans[c] += 1
        return ans

    g_map = count_sym(g)

    ans = 0
    for i in range(Slen-glen):
        tmp = count_sym(S[i:i+glen])
        if tmp == g_map:
            ans += 1

    print(ans)


if __name__ == '__main__':
    task_H()