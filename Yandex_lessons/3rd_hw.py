def task_B():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    ht = dict()
    for item in first:
        if item not in ht:
            ht[item] = None

    ans = sorted([x for x in second if x in ht])
    print(' '.join([str(x) for x in ans]))

def task_E():
    xyz = input().split()
    N = input()

    ans = 0
    for n in set(N):
        if n not in xyz:
            ans += 1
            
    print(ans)


if __name__ == "__main__":
    task_E()